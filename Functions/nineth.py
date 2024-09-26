listTuple=[('English',88),('Science',90),('Maths',97),('Social sciences',82)]
def compareByInt(lsTp):
    return sorted(lsTp,key=lambda x:x[1])
print(compareByInt(listTuple))