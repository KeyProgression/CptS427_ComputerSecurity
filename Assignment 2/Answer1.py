Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Cypherbet = 'SUNDIVERABCFLHJKZMOPQTWGYX'
Shiftedbet = 'IJKDGLMNEOPXRCSTUHAVBFWZYQ'

# Tests all possible left shifts to find our monoalphanetoc cipher
def BruteForceCipher(plainText):
    for key in range(len(Alphabet)):
        translated = ''
        for move in plainText:
            if move == '?' or move == ' ':
                pass
            elif move in Alphabet:
               shift = Alphabet.find(move)
               shift = shift - key
               if shift < 0:
                   shift = shift + len(Alphabet)
               translated = translated + Alphabet[shift]
            else:
                translated = translated + move
        print('KEY #%s: %s' % (key, translated))


#BruteForceCipher('ACVLQDMZ')
#Key 8: Right shift = 8


