#!/bin/bash

# Run this by "./test.sh"
py run.py --directory ./data --type aes --secrets secrets --action encrypt
py run.py --directory ./data_result --type aes --secrets secrets --action decrypt

py test.py