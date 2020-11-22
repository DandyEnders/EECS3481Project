from cryptography.fernet import Fernet
import rsa
from Crypto.Cipher import Blowfish
from Crypto.Cipher import ARC4
from itertools import cycle

import hashlib
from Crypto.Cipher import AES

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad


class CipherMethod:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plain_byte: bytes) -> bytes:
        pass

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        pass


class XORCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        self.key = key.encode('utf-8')

    def encrypt(self, plain_byte: bytes) -> bytes:
        return bytes([_a ^ _b for _a, _b in zip(plain_byte, cycle(self.key))])

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        return bytes([_a ^ _b for _a, _b in zip(encrypted_byte, cycle(self.key))])


class AESCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        self.block_size = AES.block_size
        self.byte_key = hashlib.sha256(key.encode()).digest()
        self.iv = (" " * self.block_size).encode()

    def encrypt(self, plain_byte: bytes) -> bytes:
        encrypter = AES.new(self.byte_key, AES.MODE_CBC, iv=self.iv)
        encrypted_byte = encrypter.encrypt(pad(plain_byte, self.block_size))
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        decrypter = AES.new(self.byte_key, AES.MODE_CBC, iv=self.iv)
        plain_byte = unpad(decrypter.decrypt(encrypted_byte), self.block_size)
        return plain_byte


class RC4Cipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)

    def encrypt(self, plain_byte: bytes) -> bytes:
        arc4 = ARC4(self.key.encode())
        encrypted_byte = arc4.encrypt(plain_byte)
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        arc4 = ARC4(self.key.encode())
        plain_byte = arc4.decrypt(encrypted_byte)
        return plain_byte


class BlowFishCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        self.block_size = Blowfish.block_size
        self.byte_key = hashlib.sha256(key.encode()).digest()
        self.iv = (" " * self.block_size).encode()

    def encrypt(self, plain_byte: bytes) -> bytes:
        encrypter = Blowfish.new(self.byte_key, Blowfish.MODE_CBC, iv=self.iv)
        encrypted_byte = encrypter.encrypt(pad(plain_byte, self.block_size))
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        decrypter = Blowfish.new(self.byte_key, Blowfish.MODE_CBC, iv=self.iv)
        plain_byte = unpad(decrypter.decrypt(encrypted_byte), self.block_size)
        return plain_byte


class RSACipher(CipherMethod):
    # encrypt with one key, decrypt with another
    # rsa slow so use symmetrci for encryption and then rsa to encrypt the key
    # can only encrypt something thats only the size of the key or less
    # each time run functions generates new pub and priv key therefore decryption is hard
    # therefore use rsa to encrypt the key that is used for encryption and decryption
    # encrypt file with symmetric encryption and encrypt keys with asymetric encryption

    def __init__(self, key):
        super().__init__(key)
        sym_key_file = open('./src/rsaKeys/symmetric.key', 'rb')
        self.symKey = sym_key_file.read()
        # create the cipher
        self.cipher = Fernet(self.symKey)
        pub_key_file = open('./src/rsaKeys/publicKey.key', 'rb')
        pub_key_file_read = pub_key_file.read()
        # special format for loading in pub key for rsa
        self.pubKey = rsa.PublicKey.load_pkcs1(pub_key_file_read)
        # encrypt the sym key file with pub key
        self.encrypted_key = rsa.encrypt(self.symKey, self.pubKey)
        # write the encrypted symm key to a file
        ekey = open('./src/rsaKeys/encrypted_key', 'wb')
        ekey.write(self.encrypted_key)
        # load private key to decrypt the public key
        prkey = open('./src/rsaKeys/privkey.key', 'rb')
        pkey = prkey.read()
        self.private_key = rsa.PrivateKey.load_pkcs1(pkey)
        self.decrypted_public_key = rsa.decrypt(
            self.encrypted_key, self.private_key)
        self.cipher2 = Fernet(self.decrypted_public_key)

    def encrypt(self, plain_byte: bytes) -> bytes:
        encrypted = self.cipher.encrypt(plain_byte)
        return encrypted

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        # decrypt encrypted public key with private key to decrypt the file
        decrypted_data = self.cipher2.decrypt(encrypted_byte)
        return decrypted_data


class ECCCipher(CipherMethod):
    def __init__(self, key):
        pass

    def encrypt(self, plain_byte: bytes) -> bytes:
        encrypted_byte = plain_byte  # TODO
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        plain_byte = encrypted_byte  # TODO
        return plain_byte
