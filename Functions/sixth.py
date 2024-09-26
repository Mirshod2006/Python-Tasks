def makeDictionary(list):
    dictionary = {}
    for i in range(len(list)):
        dictionary[list[i][0]] = [list[i][1],list[i][2]]
    print(dictionary)
ls=[[1,'Jean Castro','V'],[2,'Lula Rowel','V'],[3,'Brain Howell','VI'],[4,'Lynne Foster','VI'],[5,'Zachary Simon','VII']]
makeDictionary(ls)