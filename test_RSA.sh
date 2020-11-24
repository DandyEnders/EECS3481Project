#!/bin/bash

# Run this by "./test.sh"
python3 run.py --directory ./data --type rsa --privateKey EECS3481Alice --publicKey abc --action encrypt
python3 run.py --directory ./data_result --type rsa --privateKey EECS3481Bob --publicKey abc --action decrypt

python3 test.py