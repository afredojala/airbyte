#!/bin/sh

rm res.json

python main.py read --config sample_files/config.json --catalog sample_files/configured_catalog_incremental.json > res.json
