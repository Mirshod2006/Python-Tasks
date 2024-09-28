try:
    with open('Phone.txt','r') as phone_numbers:
        operators=[{'beeline':[],'ucell':[],'uzmobile':[],'uztelecom':[],'humans':[],'ums':[],'rostelecom':[],'mts':[],'megafon':[]}]
        operator_map ={'1':'beeline','2':'ucell','3':'uzmobile','4':'uztelecom',
                   '5':'humans','6':'ums','7':'rostelecom','8':'mts','9':'megafon'}
        for line in phone_numbers:
            line=line.strip()
            operators[0][operator_map[line.split(" ")[-1][0]]].append(line.split(" ")[-1])
        print(*operators,sep=" ")
except Exception as e:
    print(f"An error occurred: {e}")