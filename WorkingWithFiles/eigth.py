def giveSortedWords(words,reverse):
    word_list = [word for word in words]
    word_list.sort(reverse=reverse)
    word_str= "".join(word+" " for word in word_list)
    return word_str
    
inp = input("Enter words:")
try:
    with open("new1.txt",'w') as file1:
        file1.write(giveSortedWords(inp,True))
except Exception as e:
    print(f"An error occurred: {e}")

try:
    with open("new2.txt",'w') as file2:
        file2.write(giveSortedWords(inp,False))
except Exception as e:
    print(f"An error occurred: {e}")