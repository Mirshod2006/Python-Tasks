def fivePrime(num):
    numbers=[]
    count=5

    if num % 2 == 0:
        num += 1

    while True:
        prime = True
        for i in range(2,num):
            if num%i==0:
                prime = prime & False
                break
        if prime:
            numbers.append(num)
            count-=1
        if count==0:
            break
        num +=2
    print(*numbers,sep=" ")
num = int(input("Enter number:"))
fivePrime(num)