# Author: Matthew Yien
# StuID : 11698797
# Problem: Analyze the entries in password1.txt, how many entries? What is the most commonly used password?
#          Which user has the most login failed attempts? What is the common salt, used for the password2.txt?

import hashlib as ha


# starts from the 4th index and grabs every 6th element from there which should be every password
def ParsePassword(fileName):
    with open(fileName, "rt") as f:
        newL = f.read()
        entry = newL.split(",")
    returnList = entry[4::6]
    return returnList

# Goes through a .txt file and splits it at the end of the line and returns to a list
def ParseWordList(fileName):
    with open(fileName, "rt") as f:
        newL = f.read()
    return newL.split("\n")

# finds total entries of a file
def passwordEntry(fileName):
    entry = ParseWordList(fileName)
    counter = 0

    for l in entry:
        if l:
            counter += 1
    return counter

# finds most commonly used password, O(n). Could use a hashtable to make faster
def PasswordCount(fileName):       
    passwordList = ParsePassword(fileName)
    passwordCount = {}
    
    for password in passwordList:
        if password in passwordCount.keys():
            passwordCount[password] += 1
        else:
            passwordCount[password] = 1
    return max(passwordCount,key=passwordCount.get)

# only works for password2.txt
def FindSalt(fileName):
    passwordParsedList = ParsePassword(fileName)
    listOfWords = ParseWordList("wordList.txt")
    # just need to get one right for the salt
    for password in listOfWords:
        for salt in listOfWords:
            if ha.md5((password+salt).encode()).hexdigest() in passwordParsedList:
                return salt

numberEntry = passwordEntry("password1.txt")
mostUsedPw = PasswordCount("password1.txt")
saltThatWasAdded = FindSalt("password2.txt")

print("There are ", numberEntry, " entries in password1.txt")
print("The most used password is ", mostUsedPw)
print("Salt that was added to every password is: ", saltThatWasAdded)

# Testing idahosaturn
#hexDigest = '81d4ce3fd1613924ed42bb4928c7e645'
#tstDigest = "idahosaturn"
#if ha.md5(tstDigest.encode()).hexdigest() == hexDigest:
#    print("True")
