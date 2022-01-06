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
    cursor_field = "timestamp_added"
    primary_key  = None
    data_field = "data"

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
    ) -> Iterable[MutableMapping]:
        json_response = response.json()
        yield from json_response.get(self.data_field, [])

class SourceHeliumApi(AbstractSource):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        return True, None

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        auth = NoAuth()
        date = datetime.strptime(config['date'], '%Y-%m-%dT%H:%M:%S')
        return [HeliumHotspots(authenticator = auth, date = date)]
