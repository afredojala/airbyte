#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_helium_api import SourceHeliumApi

if __name__ == "__main__":
    source = SourceHeliumApi()
    launch(source, sys.argv[1:])
