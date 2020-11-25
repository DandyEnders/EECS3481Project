#!/bin/bash

# python3 generate_keys.py

KIND="ecc"
SENDER="alice"
RECEIVER="bob"

cd keys

cd ..

# Run this by "./test.sh"
python3 run.py --directory ./data --type $KIND --sender "$SENDER" --receiver "$RECEIVER" --action encrypt
python3 run.py --directory ./data_result --type $KIND --sender "$RECEIVER" --receiver "$SENDER" --action decrypt

python3 test.py