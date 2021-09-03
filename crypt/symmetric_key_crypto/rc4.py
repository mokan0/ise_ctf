# p.271-の写経
# Ronald Rivestによって開発されたストリーム暗号
# ARC4と呼ばれる

def KSA(key):
    """
    Key Schedule Algorithm
    鍵を内部状態に変換する
    srandに相当
    """
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j+S[i]+key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PRGA(S):
    """
    Preseudo-Random Generation Algorithm
    KSAで生成した内部状態を基に，内部状態のかき混ぜと
    １バイトの乱数出力を繰り返す
    randに相当
    """
    S = S[:]
    i = 0
    j = 0
    while True:
        i = (i+1) % 256
        j = (j+S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key = S[(S[i]+S[j]) % 256]
        yield key


def xor(a, b):
    return a ^ b


plaintext = b'helloworld'
S = KSA(b'testkey')
# print(S)
# PRGAからの乱数と平文をXOR
ciphertext = bytes(map(xor, plaintext, PRGA(S)))
print(ciphertext)
# b'\xf4\xe7\xd2x-\x84Qe\xc9Q'
plaintext2 = bytes(map(xor, ciphertext, PRGA(S)))
print(plaintext2)
# b'helloworld'
