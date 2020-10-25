from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack

import hashlib
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

import Crypto
from Crypto.Cipher import AES
# hashes the key (password) into a 32 byte value
from Crypto.Hash import SHA256


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
        # TODO

    def encrypt(self, plain_byte: bytes) -> bytes:
        # print("encrypting")
        encrypted_byte = plain_byte  # TODO, encrypt plain_byte
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        # print("decrypting")
        plain_byte = encrypted_byte  # TODO, decrypt plain_byte
        return plain_byte


class AESCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        hash_obj = SHA256.new(key.encode('utf-8'))
        self.cipher = hash_obj.digest()  # the key now made 32 bytes long

    def encrypt(self, plain_byte: bytes) -> bytes:
        print("encrypting")
        message = plain_byte
        BLOCK_SIZE = 16
        PAD = bytes('{', encoding="ascii")
        def padding(v): return v + (BLOCK_SIZE - len(v) % BLOCK_SIZE) * PAD
        cipher = AES.new(self.cipher, AES.MODE_ECB)
        encrypted_byte = cipher.encrypt(padding(message))
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        print("decrypting")
        message = encrypted_byte
        PAD = bytes('{', encoding="ascii")
        decipher = AES.new(self.cipher, AES.MODE_ECB)
        decrypt_pt = decipher.decrypt(message)
        pad_index = decrypt_pt.find(PAD)
        plain_byte = decrypt_pt[:pad_index]
        return plain_byte


class RC4Cipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        # TODO

    def encrypt(self, plain_byte: bytes) -> bytes:
        # print("encrypting")
        encrypted_byte = plain_byte  # TODO, encrypt plain_byte
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        # print("decrypting")
        plain_byte = encrypted_byte  # TODO, decrypt plain_byte
        return plain_byte


class BlowFishCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        self.block_size = Blowfish.block_size
        self.iv = Random.new().read(self.block_size)
        byte_key = str.encode(key)
        byte_key = hashlib.sha256(key.encode()).digest()
        self.cipher = Blowfish.new(byte_key,
                                   Blowfish.MODE_CBC,
                                   self.iv)

    def encrypt(self, plain_byte: bytes) -> bytes:
        # print("encrypting")
        plen = self.block_size - divmod(len(plain_byte), self.block_size)[1]
        padding = [plen]*plen
        padding = pack('b'*plen, *padding)
        encrypted_byte = self.iv + self.cipher.encrypt(plain_byte + padding)
        return encrypted_byte

    def decrypt(self, encrypted_byte: bytes) -> bytes:
        # print("decrypting")
        ciphertext = encrypted_byte
        ciphertext = ciphertext[self.block_size:]
        plain_byte = self.cipher.decrypt(ciphertext)
        last_byte = plain_byte[-1]
        plain_byte = plain_byte[:- (last_byte if type(last_byte)
                                    is int else ord(last_byte))]
        return plain_byte
