month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
def targetDate(date):
    changedDateForm=""
    ls=date.split(".")
    changedDateForm +=ls[0]+" "
    changedDateForm +=month_dict[int(ls[1])]+" "
    year = ls[2].split(" ")[0]
    hour = ls[2].split(" ")[1].split(":")[0]
    minute = ls[2].split(" ")[1].split(":")[1]
    changedDateForm +=year+" year "+hour+" hours "+minute+" minutes"
    print(changedDateForm)
targetDate("01.01.2000 00:00")