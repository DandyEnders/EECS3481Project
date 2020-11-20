#!/bin/bash

# Run this by "./test.sh"
py run.py --directory ./data --type ecc --secrets EECS3481 --action encrypt
py run.py --directory ./data_result --type ecc --secrets EECS3481 --action decrypt

py test.py