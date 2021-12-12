#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_helium_account_hotspots import SourceHeliumAccountHotspots

if __name__ == "__main__":
    source = SourceHeliumAccountHotspots()
    launch(source, sys.argv[1:])
