def takeID(line):

    words=line.split(" ")
    # Loops through words
    if is_repeated_numbers("".join(words[len(words)-1]).replace(".","")):# I know the form of data
                                # So just taking the last element of the list and checking it
        print(line)

def is_repeated_numbers(number_string):
    # A set is created
    seen = set()
    # Loop through each digit in the number string
    for digit in number_string:
        # If digit already in the set, it means it is repeated
        if digit in seen:
            return False # So, we are returning False
        seen.add(digit) # Updating that set 
    return True
try:
    # When opening file I got continues errors and then by taking help from AI 
    # I found out that File was not in Readable format then I added UTF-8
    with open("Countries.txt","r",encoding='utf-8',errors='ignore') as file:
        # f_line = file.readline()
        # takeID(f_line)
        for line in file:
            line = line.strip()
            takeID(line)
except Exception as e:
    print(f"Error occurred : {e}")

