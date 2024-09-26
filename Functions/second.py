def convertToMap(str):
    ls=[j for j in str]
    letterDict=dict()
    for i in ls:
        letterDict[i]=ls.count(i)
    print(letterDict)
convertToMap(input("Enter string:"))