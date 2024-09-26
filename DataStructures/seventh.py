def makeCapital(letter,word):
    if letter in word:
        return word.replace(letter,letter.upper())
word = input("Enter word:")
letter=input("Enter letter:")
print(makeCapital(letter,word))