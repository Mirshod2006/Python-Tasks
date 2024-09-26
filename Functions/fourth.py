def showSeparation(str):
    # Split the string into words
    words = str.split()
    sentences=str.split(".")
    print(*words)
    print(sentences)
showSeparation(input("Enter string:"))