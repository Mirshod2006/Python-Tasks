try:
    with open("someFile.txt",'r') as file1:
        sum_str=""
        for line in file1:
            num_str=""
            for ch in line:
                if ch.isdigit():
                    num_str+=ch
                elif num_str!="":
                    sum_str+=num_str
                    sum_str+="+"
                    num_str=""
            if num_str!="":
                sum_str+=num_str
        print(sum_str)
except Exception as e:
    print(f"An error occurred: {e}")
