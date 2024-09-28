def giveSortedNumbers(numbers,reverse):
    number_list = [number for number in numbers]
    number_list.sort(reverse=reverse)
    number_str= "".join(number+" " for number in number_list)
    return number_str
    
inp = input("Enter numbers:")
try:
    with open("new1.txt",'w') as file1:
        file1.write(giveSortedNumbers(inp,True))
except Exception as e:
    print(f"An error occurred: {e}")

try:
    with open("new2.txt",'w') as file2:
        file2.write(giveSortedNumbers(inp,False))
except Exception as e:
    print(f"An error occurred: {e}")