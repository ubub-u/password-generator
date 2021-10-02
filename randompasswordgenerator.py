import random

def main():
    startover = True
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

    passwordgenerator(usernum, userletter, usersymbol)


    


def passwordgenerator(numnum, numletter, numsymbol):
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

    for each in range(0, numletter):
        charactersforpassword.append(numarray[random.randint(0,len(numarray)-1)])

    for each in range(0, numnum):
        charactersforpassword.append(letterarray[random.randint(0,len(letterarray)-1)])

    for each in range(0, numsymbol):
        charactersforpassword.append(symbolarray[random.randint(0, len(symbolarray)-1)])

    random.shuffle(charactersforpassword)

    for each in charactersforpassword:
        finalpassword += each

    print(finalpassword)

if __name__ == '__main__':
    main()