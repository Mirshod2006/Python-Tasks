def changePosition(dictionary):
    keys=list(dictionary.keys())
    if len(dictionary)%2==0:
        for i in range(0,len(keys),2):
            dictionary[keys[i]],dictionary[keys[i+1]] = dictionary[keys[i+1]],dictionary[keys[i]]
    else:
        for i in range(0,len(keys)-1,2):
            dictionary[keys[i]],dictionary[keys[i+1]]=dictionary[keys[i+1]],dictionary[keys[i]]
    print(dictionary)
dictionary = {1:'ABC',2:'DEF',3:'GHI',4:'JKL',5:'MNO'}
changePosition(dictionary)