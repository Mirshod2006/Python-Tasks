def makeSentence():
    sentence =""
    count=4
    print("Enter numbers[ 0 for cancel]:")
    capital=True
    while True:
        word=input()
        if word == "0":
            break
        
        if capital:
            sentence += word.capitalize()
        else:
            sentence += word

        if count == 0:
            sentence+="."
            capital=True
            count=5
        else:
            sentence+=" "
            capital=False
        count-=1
    print(sentence)
makeSentence()