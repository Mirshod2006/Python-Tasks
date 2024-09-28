def checkAlphas(file):
    count=0
    for line in file:
        line=line.strip()
        for char in line:
            if char.isalpha():
                count+=1
    print(count)

try:
    with open("second.py",'r') as code:
        checkAlphas(code)
except Exception as e:
    print(f"An error occurred: {e}")