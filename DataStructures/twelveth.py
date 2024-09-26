import itertools

def all_permutations(input_list):
    # Generate all permutations of the input list
    perms = list(itertools.permutations(input_list))
    perms_as_lists = [list(perm) for perm in perms]
    return perms_as_lists
lst=input("Enter list:")
numLst=list()
for i in lst:
    if i.isdigit():
        numLst.append(int(i))
print(all_permutations(numLst))