#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


from abc import ABC
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple
from datetime import datetime, timedelta

import requests
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.sources.streams.http import HttpStream
from airbyte_cdk.sources.streams.http.auth import NoAuth

"""
TODO: Most comments in this class are instructive and should be deleted after the source is implemented.

This file provides a stubbed example of how to use the Airbyte CDK to develop both a source connector which supports full refresh or and an
incremental syncs from an HTTP API.

The various TODOs are both implementation hints and steps - fulfilling all the TODOs should be sufficient to implement one basic and one incremental
stream from a source. This pattern is the same one used by Airbyte internally to implement connectors.

The approach here is not authoritative, and devs are free to use their own judgement.

There are additional required TODOs in the files within the integration_tests folder and the spec.json file.
"""
class CoinGecko(HttpStream):
    url_base = "https://api.coingecko.com/api/v3/coins/"
    # Set this as a noop.
    primary_key = None
    cursor_field = "date"
    def __init__(self, id: str,start_date: datetime, **kwargs):
        super().__init__()
        self.id = id
        self.start_date = start_date

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        # The API does not offer pagination, so we return None to indicate there are no more pages in the response
        return None

    def request_params(
            self,
            stream_state: Mapping[str, Any],
            stream_slice: Mapping[str, Any] = None,
            next_page_token: Mapping[str, Any] = None,
    ) -> MutableMapping[str, Any]:
        # The api requires that we include the base currency as a query param so we do that in this method
        return {'date': stream_slice["date"]}

    def path(
        self, 
        stream_state: Mapping[str, Any] = None, 
        stream_slice: Mapping[str, Any] = None, 
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return f"{self.id}/history"

    def parse_response(
        self,
        response: requests.Response,
        stream_state: Mapping[str, Any],
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None,
    ) -> Iterable[Mapping]:
        data = response.json()
        data["date"] = stream_slice["date"]
        return [data]

    def get_updated_state(self, current_stream_state: MutableMapping[str, Any], latest_record: Mapping[str, Any]) -> Mapping[str, any]:
        # This method is called once for each record returned from the API to compare the cursor field value in that record with the current state
        # we then return an updated state object. If this is the first time we run a sync or no state was passed, current_stream_state will be None.
        if current_stream_state is not None and 'date' in current_stream_state:
            current_parsed_date = datetime.strptime(current_stream_state['date'], '%d-%m-%Y')+timedelta(days=1)
            return {'date': current_parsed_date.strftime('%d-%m-%Y')}
        else:
            return {'date': self.start_date.strftime('%d-%m-%Y')}

    def _chunk_date_range(self, start_date: datetime) -> List[Mapping[str, any]]:
        """
        Returns a list of each day between the start date and now.
        The return value is a list of dicts {'date': date_string}.
        """
        dates = []
        while start_date < datetime.now():
            dates.append({'date': start_date.strftime('%d-%m-%Y')})
            start_date += timedelta(days=1)
        return dates

    def stream_slices(self, sync_mode, cursor_field: List[str] = None, stream_state: Mapping[str, Any] = None) -> Iterable[
        Optional[Mapping[str, any]]]:
        start_date = datetime.strptime(stream_state['date'], '%d-%m-%Y') if stream_state and 'date' in stream_state else self.start_date
        return self._chunk_date_range(start_date)

class SourceCoingecko(AbstractSource):

    def check_connection(self, logger, config) -> Tuple[bool, Any]:
        accepted_ids = {"helium"}
        input_id = config["id"]
        if input_id not in accepted_ids:
            return False, f"Id {input_id} not in accepted list"
        return True,None
    def streams(self, config: Mapping[str,Any]) -> List[Stream]:
        auth = NoAuth()
        start_date = datetime.strptime(config['start_date'], "%Y-%m-%d")
        return [CoinGecko(authenticator=auth,id=config["id"],start_date=start_date)]
    