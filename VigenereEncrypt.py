__author__ = 'Michal Rzezniczek'
key = 'klamstwo'
plainTextFileName = 'plainText.txt'
cipherTextFileName = 'cipherText.txt'


def encrypt(plainletter, keyletter):
    sth = (ord(plainletter) - 97 + ord(keyletter) - 97) % 26
    return str(unichr(sth + 97))


i = 0
cipherTextFile = open(cipherTextFileName, 'w')
with open(plainTextFileName, 'r') as plainTextFile:
    plainText = plainTextFile.read()
    for c in plainText:
        if i >= len(key):
            i = 0
        #tmp = str(unichr(((ord(c) + ord(key[i] - 97 - 97)) % 26)+97))
        cipherTextFile.write(encrypt(c, key[i]))
        i += 1

plainTextFile.close()
cipherTextFile.close()