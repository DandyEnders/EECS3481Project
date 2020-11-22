import rsa
from cryptography.fernet import Fernet
from rsa.key import PublicKey

# creates the symmetric key
key = Fernet.generate_key()

# write sym key to a file
k = open('./src/rsaKeys/symmetric.key', 'wb')
k.write(key)
k.close()

# create the pub and priv keys
(pubkey, privkey) = rsa.newkeys(2048)

# write the public key to a file
pukey = open('./src/rsaKeys/publickey.key', 'wb')
pukey.write(pubkey.save_pkcs1('PEM'))
pukey.close()

# write the priv key to a file
prkey = open('./src/rsaKeys/privkey.key', 'wb')
prkey.write(privkey.save_pkcs1('PEM'))
prkey.close()
