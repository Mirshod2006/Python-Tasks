def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    # index = 0
    # for guest in arrivals:
    #     if name == arrivals[-1]:
    #         return False
    #     elif guest == name:
    #         index +=1
    #         print(index)
    #         break
    #     index +=1
    # if float(index) > len(arrivals)/2 if len(arrivals)%2==0 else (len(arrivals)+1)/2:
    #     print((len(arrivals)+1)/2)
    #     return True
        
    # return False
    midpoint = (len(arrivals) + 1) // 2
    for i, guest in enumerate(arrivals):
        if arrivals[-1] == name:
            return False
        if guest == name:
            return i >= midpoint
    return False

arrivals=['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
name = 'May'
print(fashionably_late(arrivals,name))