from Crypto import Cipher
from Crypto.Cipher import ARC4
cipher = ARC4.new(b'secretkey')
encrypted = cipher.encrypt(b'{"usename": "user1"}')
# b'\xde\x8a\xa9o)\xdf\xf4%M\x8eq\xa4\xa0RFN\x06f+\x1d'
# user1 -> admin
bitflip = bytearray(encrypted)
# bytearray型だと代入が可能


bitflip[13] ^= ord('u') ^ ord('a')
bitflip[14] ^= ord('s') ^ ord('d')
bitflip[15] ^= ord('e') ^ ord('m')
bitflip[16] ^= ord('r') ^ ord('i')
bitflip[17] ^= ord('1') ^ ord('n')

# RC4を初期化
Cipher = ARC4.new(b'secretkey')
print(Cipher.decrypt(bitflip))
