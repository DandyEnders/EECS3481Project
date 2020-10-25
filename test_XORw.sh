#!/bin/bash

# Run this by "./test.sh"
python run.py --directory ./data --type xor --secrets EECS3481 --action encrypt
python run.py --directory ./data_result --type xor --secrets EECS3481 --action decrypt

python test.py