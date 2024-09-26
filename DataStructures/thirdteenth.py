def putInIncrease(input_list):
    ls = ""
    for i in range(len(input_list) - 1):  
        if input_list[i + 1] >= input_list[i]:
            ls += str(input_list[i]) + ","
        elif ls != "":
            ls += str(input_list[i])  
            print(ls)
            ls = ""
    
    if ls != "":  
        ls += str(input_list[-1])
        print(ls)


lst = input("Enter list: ")


numLst = [int(x) for x in lst.split(',') if x.strip().lstrip('-').isdigit()]

putInIncrease(numLst)
