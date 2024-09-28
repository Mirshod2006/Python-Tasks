import csv

def showSortedList(data):
    # Sort the data in ascending order
    sortedData = sorted(data)
    # Print the sorted data
    for s_data in sortedData:
        print(*s_data)

try:
    with open('Name_list.csv','r') as names:
        reader = csv.reader(names)
        showSortedList(reader)

except Exception as e:
    print(f"An error occurred: {e}")