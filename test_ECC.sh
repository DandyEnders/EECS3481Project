#!/bin/bash

# python3 generate_keys.py

KIND="ecc"
SENDER="alice"
RECEIVER="bob"

cd keys

# SENDER_PRIVATE_KEY=`python3 get_keys.py --name $SENDER --kind $KIND --type private`
# SENDER_PUBLIC_KEY=`python3 get_keys.py --name $SENDER --kind $KIND --type public`

# RECEIVER_PRIVATE_KEY=`python3 get_keys.py --name $RECEIVER --kind $KIND --type private`
# RECEIVER_PUBLIC_KEY=`python3 get_keys.py --name $RECEIVER --kind $KIND --type public`

cd ..

# Run this by "./test.sh"
python3 run.py --directory ./data --type $KIND --sender "$SENDER" --receiver "$RECEIVER" --action encrypt
python3 run.py --directory ./data_result --type $KIND --sender "$RECEIVER" --receiver "$SENDER" --action decrypt

python3 test.py