#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_helium_rewards import SourceHeliumRewards

if __name__ == "__main__":
    source = SourceHeliumRewards()
    launch(source, sys.argv[1:])
