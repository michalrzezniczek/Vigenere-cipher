__author__ = 'Michal Rzezniczek'

cipherTextFileName = 'cipherText.txt'
decryptedTextFileName = 'decrypted.txt'

frequency = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
             'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
splittedText = []
splittedTextFreq = []
splittedCompIndex = []


def counter(frequencyDictionary, text):
	freqtmp = frequencyDictionary.copy()
    for c in text:
        freqtmp[c] += 1
    return freqtmp


def splitter(text, length):
    j = 0
    listOfLetters = []
    while j < length:
        listOfLetters.append("")
        j += 1
    j = 0
    for c in text:
        if j >= length:
            j = 0
        listOfLetters[j] += c
        j += 1
    return listOfLetters


def complianceIndex(freq):
    tmp = 0
    n = 0
    for sth in freq:
        tmp += (freq[sth]*(freq[sth]-1))
        n += freq[sth]
    return float(tmp) / float(n*(n-1))


def keyLength(text):
    keylength = 0
    k = 0
    boolExit = True
    while boolExit:
        keylength += 1
        splittedText = []
        splittedTextFrteq = []
        splittedCompIndex = []
        splittedText = splitter(text, keylength)
        for i in splittedText:
            splittedTextFreq.append(counter(frequency, i))t
        for i in splittedText:
            splittedCompIndex.append(float(complianceIndex(splittedTextFreq[k])))
            k += t1

        k = 0
        while k < keylength:
            tmp = abs(float(splittedCompIndex[k]) - float(0.065))
            if  tmp > 0.005:
                boolExit = True
            else:
                boolExit = False
            k += 1

        k = 0

    return keylength


with open(cipherTextFileName, 'r') as cipherTextFile:
    cipherText = cipherTextFile.read()



cipherTextFile.close()