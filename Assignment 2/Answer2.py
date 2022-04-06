Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Cypherbet = 'SUNDIVERABCFLHJKZMOPQTWGYX'
Shiftedbet1 = 'STUVWXYZABCDEFGHIJKLMNOPQR'
Shiftedbet2 = 'IJKDGLMNEOPQRCSTUHAVBFWXYZ'

# Decrypt's Text to a file named Question2_translated.txt
# Decrypts using a monoalphabetic substitution cipher, cipher made using a crpytanalysis tool of letters ordered by most common appearance of encrypted text
def DecryptTxt(fileName):
    data = ''
    with open(fileName, 'r') as file:
        data = file.read()
    translate = ''
    for symbol in data:
        if symbol == '?':
            translate += ' '
        elif symbol == '\n':
            translate += '\n'
        elif symbol == '\r':
            translate += '\r'
        else:
            translate += Shiftedbet2[Alphabet.index(symbol)]
    with open("Question2_translated.txt", "w") as myFile:
        myFile.write(translate)
    print(f'Done decrypting')

def BFCW(plainText):
    for key in range(len(Cypherbet)):
        translated = ''
        for move in plainText:
            if move not in Cypherbet:
                pass
            elif move in Cypherbet:
               shift = Cypherbet.find(move)
               shift = shift - key
               if shift < 0:
                   shift = shift + len(Cypherbet)
               translated = translated + Cypherbet[shift]
            else:
                translated = translated + move
        print('KEY #%s: %s' % (key, translated))
