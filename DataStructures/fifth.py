def convertBinary(num):
    binaryStr = bin(num).replace("0b","")
    count=0
    for i in binaryStr:
        if i == '0':
            count += 1
    print(count)
number = int(input("Enter number to get binary zeros:"))
convertBinary(number)