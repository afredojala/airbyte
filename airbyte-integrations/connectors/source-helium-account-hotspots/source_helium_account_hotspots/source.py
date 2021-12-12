#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


from abc import ABC
from datetime import datetime
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple

import requests
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.sources.streams.http import HttpStream
from airbyte_cdk.sources.streams.http.auth import NoAuth

class HeliumAccountsHotspots(HttpStream):
    url_base = "https://api.helium.io/v1/"
    cursor_field = "date"
    primary_key = "date"

    def __init__(self, account_id: str, start_date: str, **kwargs) -> None:
        super().__init__()
        self.account_id = account_id
        self.date = start_date

    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
        ) -> str:
        return f"accounts/{self.account_id}/hotspots"

    def request_params(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
        ) -> MutableMapping[str, Any]:
       return None

    def parse_response(
        self,
        response: requests.Response,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> Iterable[Mapping]:
        return [response.json()]

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        # TODO: Fix Pagination!
        return None


class SourceHeliumAccountHotspots(AbstractSource):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        return True, None

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        auth = NoAuth()
        start_date = datetime.strptime(config["start_date"], "%Y-%m-%d")
        return [HeliumAccountsHotspots(authenticator=auth, account_id=config["account_id"], start_date=start_date)]

