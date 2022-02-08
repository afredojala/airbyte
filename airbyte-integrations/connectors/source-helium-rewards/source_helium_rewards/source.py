#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


from abc import ABC
from datetime import datetime, timedelta
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple

import requests
from requests import status_codes
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.sources.streams.http import HttpStream
from airbyte_cdk.sources.streams.http.auth import NoAuth



class HeliumRewards(HttpStream):
    url_base = "https://api.helium.io/v1/rewards/sum"
    data_field = 'data'
    cursor_field = 'timestamp'
    raise_on_http_errors = False
    primary_key = None

    def __init__(self, start_date: datetime, **kwargs) -> None:
        super().__init__()
        self.start_date = start_date
        self.interval = timedelta(days=1)
        

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        if response.status_code != 200:
            return None
        decoded_response = response.json()
        if len(decoded_response["data"]) == 0:
            return 0

        if 'cursor' in decoded_response.keys():
            return {"cursor" : decoded_response["cursor"]}
        return None 


    def path(
        self, 
        stream_state: Mapping[str, Any] = None, 
        stream_slice: Mapping[str, Any] = None, 
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return None


    def request_params(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None,
    ) -> MutableMapping[str, Any]:
        params = {
            "min_time" :stream_slice["min_time"],
            "max_time" :stream_slice["max_time"],
            "bucket" : "day"
        }
        if next_page_token:
            params.update(**next_page_token)
        return params

    def parse_response(
        self,
        response: requests.Response,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None,
    ) -> Iterable[MutableMapping]:
        if response.status_code!= 200:
            yield from []
        
        json_response = response.json()

        data = json_response.get(self.data_field, [])
        # data.reverse()
        yield from data

    def get_updated_state(self, current_stream_state: MutableMapping[str, Any], latest_record: Mapping[str, Any]) -> Mapping[str, any]:
        if current_stream_state is not None and 'min_time' in current_stream_state:
            current_parsed_date = datetime.strptime(current_stream_state['min_time'], '%Y-%m-%d')
            latest_record_date = datetime.strptime(latest_record["timestamp"].split("T")[0],  '%Y-%m-%d')
            new_min = max(current_parsed_date, latest_record_date)
            return {
                'min_time': new_min.strftime('%Y-%m-%d'),
                'max_time' : (new_min+self.interval).strftime('%Y-%m-%d')
            }
        else:
            return {
                'min_time': self.start_date.strftime('%Y-%m-%d'),
                'max_time': (self.start_date + self.interval).strftime('%Y-%m-%d')}


    def _chunk_date_range(self, start_date: datetime) -> List[Mapping[str, any]]:
        """
        Returns a list of each day between the start date and now.
        The return value is a list of dicts {'date': date_string}.
        """
        dates = []
        max_time = datetime.strptime(datetime.now().strftime("%Y-%m-%d"),"%Y-%m-%d")
        while start_date < max_time:
            dates.append(
                {
                    'min_time': start_date.strftime('%Y-%m-%d'),
                    'max_time': (start_date + self.interval).strftime('%Y-%m-%d')
                })
            start_date += self.interval
        return dates

    def stream_slices(self, sync_mode, cursor_field: List[str] = None, stream_state: Mapping[str, Any] = None) -> Iterable[
        Optional[Mapping[str, any]]]:
        start_date = datetime.strptime(stream_state['min_time'], '%Y-%m-%d') if stream_state and 'min_time' in stream_state else self.start_date
        return self._chunk_date_range(start_date)




class SourceHeliumRewards(AbstractSource):

    def check_connection(self, logger, config) -> Tuple[bool, any]:
        # Implement check for account
        return True, None

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        auth = NoAuth()
        start_date = datetime.strptime(config['start_date'], "%Y-%m-%d")
        return [HeliumRewards(authenticator=auth, start_date=start_date)]
