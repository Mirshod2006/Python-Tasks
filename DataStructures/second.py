def correctOrder(str):
    ls=list()
    word = ""
    for char in str:
        if char.isspace():
            ls.append(word)
            word =""
            continue
        word +=char
    ls.append(word)
    ls = set(ls)
    print(*sorted(ls))
sentence=input("Enter some order of words:")
correctOrder(sentence)

