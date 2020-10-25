from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack
from arc4 import ARC4

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
        print("encrypting")
        encrypted_byte = plain_byte # TODO, encrypt plain_byte
        return encrypted_byte
    
    def decrypt(self, encrypted_byte: bytes) -> bytes:
        print("decrypting")
        plain_byte = encrypted_byte # TODO, decrypt plain_byte
        return plain_byte
        
class AESCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        # TODO
    
    def encrypt(self, plain_byte: bytes) -> bytes:
        print("encrypting", plain_byte)
        encrypted_byte = plain_byte # TODO, encrypt plain_byte
        return encrypted_byte
    
    def decrypt(self, encrypted_byte: bytes) -> bytes:
        print("decrypting")
        plain_byte = encrypted_byte # TODO, decrypt plain_byte
        return plain_byte
        
class RC4Cipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        # TODO
    
    def encrypt(self, plain_byte: bytes) -> bytes:
        print("encrypting", plain_byte)
        arc4 = ARC4(self.key.encode('utf-8'))
        encrypted_byte = arc4.encrypt(plain_byte) # TODO, encrypt plain_byte
        return encrypted_byte
    
    def decrypt(self, encrypted_byte: bytes) -> bytes:
        print("decrypting")
        arc4 = ARC4(self.key.encode('utf-8'))
        plain_byte = arc4.decrypt(encrypted_byte) # TODO, decrypt plain_byte
        return plain_byte
        
class BlowFishCipher(CipherMethod):
    def __init__(self, key):
        super().__init__(key)
        self.block_size = Blowfish.block_size
        self.iv = Random.new().read(self.block_size)
        self.cipher = Blowfish.new(str.encode(key), 
                                   Blowfish.MODE_CBC, 
                                   self.iv)
    
    def encrypt(self, plain_byte: bytes) -> bytes:
        print("encrypting")
        plen = self.block_size - divmod(len(plain_byte), self.block_size)[1]
        padding = [plen]*plen
        padding = pack('b'*plen, *padding)
        encrypted_byte = self.iv + self.cipher.encrypt(plain_byte + padding)
        return encrypted_byte
    
    def decrypt(self, encrypted_byte: bytes) -> bytes:
        print("decrypting")
        ciphertext = encrypted_byte
        ciphertext = ciphertext[self.block_size:]
        plain_byte = self.cipher.decrypt(ciphertext)
        last_byte = plain_byte[-1]
        plain_byte = plain_byte[:- (last_byte if type(last_byte) is int else ord(last_byte))]
        return plain_byte
