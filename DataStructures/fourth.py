def checkWords(sen):
    ls=[]
    ls = sen.split()
    k=0
    for i in ls:
        if len(i)%2!=0:
            word=""
            for j in range(len(i)):
                word+=i[len(i)-1-j]
            ls[k]=word
        k+=1
    print(*ls,sep=" ")
sentence = input("Enter some sentence:")
checkWords(sentence)