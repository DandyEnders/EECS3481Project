#!/bin/bash

# Run this by "./test.sh"
python3 run.py --directory ./data --type rsa --secrets EECS3481 --action encrypt
python3 run.py --directory ./data_result --type rsa --secrets EECS3481 --action decrypt

python3 test.py