def combine_and_make_biggest(ls):
    strLs = [str(j) for j in ls]
    strLs.sort(reverse=True)
    s=""
    for i in strLs:
        s +=i
    print(s)
numLs=[61,228,9]
combine_and_make_biggest(numLs)