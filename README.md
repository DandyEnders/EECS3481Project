# EECS3481Project

# Run

Encrypt every files under the directory ./data using XORCipher with secret code "secret".
```
python3 run.py --directory ./data --type XOR --secrets secret --action encrypt 
```

Decrypt every files under the directory ./data using XORCipher with secret code "secret" .
```
python3 run.py --directory ./data --type XOR --secrets secret --action decrypt 
```

Encrypt every files under the directory ./data using AESCipher with secret code "secret" .
```
python3 run.py --directory ./data --type aes --secrets secret --action encrypt 
```

Encrypt "./data/dummy.txt" using rc4Cipher with secret code "secret" .
```
python3 run.py --directory ./data.dummy.txt --type rc4 --secrets secret --action encrypt 
```