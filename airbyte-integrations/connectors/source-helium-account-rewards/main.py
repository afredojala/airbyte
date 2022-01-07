#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_helium_account_rewards import SourceHeliumAccountRewards

if __name__ == "__main__":
    source = SourceHeliumAccountRewards()
    launch(source, sys.argv[1:])
