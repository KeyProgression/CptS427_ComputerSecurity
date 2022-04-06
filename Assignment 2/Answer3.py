import re as FunTimes


# A class running a classic vignere cipher, uses a bit of algebra
# Only needed the deciphering portion for this assignment
class LewisCarol(object):
    def __init__(self):
        self.table = self.__create_table()
    
    def __create_table(self):
        table = []
        for index in range(0,26):
            offset = 0
            row = []
            for column in range(0,26):
                row.append(chr(index + 65 + offset))
                offset += 1
                if offset > (25 - index):
                    offset = offset - 26
            table.append(row)
        return table

    """
    If you know the keyword to a Vignere cipher you can decrypt it using this method.
    """
	# (enciphered index - keyword index) mod 26
    def decipherCarol(self, cipherText, keyword):
        keywordRepeated = self.__get_keyword_repeated(keyword, len(cipherText))
        decipheredText = ""
        for index, letter in enumerate(cipherText):
            keywordIndex = ord(keywordRepeated[index]) - 65
            decipheredLetter = chr(self.table[keywordIndex].index(letter) + 65)
            decipheredText += decipheredLetter
        return "".join(decipheredText)

    def __get_keyword_repeated(self, keyword, length):
        keyword = keyword.upper()
        keywordRepeated = ""
        keywordLength = len(keyword)
        keywordIndex = 0
        for i in range(0, length):
            keywordRepeated += keyword[keywordIndex]
            keywordIndex += 1
            if keywordIndex > keywordLength - 1:
                keywordIndex = 0
        return "".join(keywordRepeated)

def main():
    cipher = LewisCarol()
    keyword = "UPLIFTWAR"
    plainText = "YSFKFMEOE"
    theAnswer = cipher.decipherCarol(plainText,keyword)
    print("%s"%(theAnswer))

main()
