import random

numarray = []
letterarray = []
symbolarray = []
juststring = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbolstring = '@%+\/!#$^?()/{/}[]'
charactersforpassword = []
finalpassword = ''
startover = True

for each in juststring:
    letterarray.append(each)

for each in range(1, 10):
    numarray.append(str(each))

for each in symbolstring:
    symbolarray.append(each)

while startover == True:
    try:
        usernum = int(input("enter num of numbers "))
        startover = False
    except:
        print("invalid input")

startover = True

while startover == True:
    try:
        userletter = int(input("enter num of letters "))
        startover = False
    except:
        print("invalid input")

startover = True

while startover == True:
    try:
        usersymbol = int(input("enter num of symbols "))
        startover = False
    except:
        print("invalid input")


for each in range(0, usernum):
    charactersforpassword.append(numarray[random.randint(0,len(numarray)-1)])

for each in range(0, userletter):
    charactersforpassword.append(letterarray[random.randint(0,len(letterarray)-1)])

for each in range(0, usersymbol):
    charactersforpassword.append(symbolarray[random.randint(0, len(symbolarray)-1)])

random.shuffle(charactersforpassword)

for each in charactersforpassword:
    finalpassword += each

print(finalpassword)