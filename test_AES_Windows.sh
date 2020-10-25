#!/bin/bash

# Run this by "./test.sh"
py run.py --directory ./data --type aes --secrets EECS3481 --action encrypt
py run.py --directory ./data_result --type aes --secrets EECS3481 --action decrypt

py test.py