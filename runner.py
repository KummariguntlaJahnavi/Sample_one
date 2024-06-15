
from datetime import date

def numOfDays(date1, date2):
	if date2 > date1: 
		return (date2-date1).days
	else:
		return (date1-date2).days

date1 = date(2024, 9, 9)
date2 =  date.today()

if date1 > date2:
    print("Your Birthday is ahead by", numOfDays(date1, date2), "days")
else:
    print("Your Birthday was", numOfDays(date1, date2), "days ago")
