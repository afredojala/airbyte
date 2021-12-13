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


class HeliumHotspots(HttpStream):
    url_base = "https://api.helium.io/v1/"
    cursor_field = "cursor"
    primary_key  = None

    def __init__(self, date: str, **kwargs) -> None:
        super().__init__()
        self.date = date

    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None,
    ) -> str:
        return "hotspots"

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        # TODO
        decoded_response = response.json()
        dates = [datetime.strptime(d["timestamp_added"].split(".")[0],"%Y-%m-%dT%H:%M:%S") < self.date for d in decoded_response["data"]]
        if sum(dates) == 0:
            return {"cursor" : decoded_response["cursor"]}

    def request_params(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None,
    ) -> MutableMapping[str, Any]:

        params = {}
        if next_page_token:
            params.update(next_page_token)
        return params

    def parse_response(
        self,
        response: requests.Response,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None,
    ) -> Iterable[Mapping]:
        return [response.json()]

    # def get_updated_state(
    #     self, current_stream_state: MutableMapping[str, Any], latest_record: Mapping[str, Any]
    # )  -> Mapping[str, Any]:
    #     if current_stream_state is not None and 'date' in current_stream_state:
    #         dates = [datetime.strptime(current_stream_state["date"],"%Y-%m-%dT%H:%M:%S")]
    #         for d in latest_record["data"]:
    #             d_test = datetime.strptime(d["timestamp_added"].split(".")[0],"%Y-%m-%dT%H:%M:%S")
    #             print(d_test)
    #             dates.append(d_test)

    #         return {"date" : min(dates)}
    #     else:
    #         return {"date" : self.date.strftime("%Y-%m-%dT%H:%M:%S")}

    # def _chunk_date_range(self, date: datetime) -> List[Mapping[str, any]]:
    #     """
    #     Returns a list of each day between the start date and now.
    #     The return value is a list of dicts {'date': date_string}.
    #     """
    #     dates = []
    #     while date < datetime.now():
    #         dates.append({'date': date.strftime('%Y-%m-%dT%H:%M:%S')})
    #         date += timedelta(days=1)
    #     return dates

    # def stream_slices(self, sync_mode, cursor_field: List[str] = None, stream_state: Mapping[str, Any] = None) -> Iterable[
    #     Optional[Mapping[str, any]]]:
    #     date = datetime.strptime(stream_state['date'], '%Y-%m-%dT%H:%M:%S') if stream_state and 'date' in stream_state else self.date
    #     return self._chunk_date_range(date)


# Source
class SourceHeliumApi(AbstractSource):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        return True, None

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        auth = NoAuth()
        date = datetime.strptime(config['date'], '%Y-%m-%dT%H:%M:%S')
        return [HeliumHotspots(authenticator = auth, date = date)]
