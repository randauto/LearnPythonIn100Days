import datetime

timeNow = datetime.datetime.now()
print(timeNow.year)
print(timeNow.month)
print(timeNow.day)

x = datetime.datetime(2023, 5, 30)
print(x.year)
print(x.month)
print(x.day)

# display the name of the month.
print(x.strftime("%B"))
print(x.strftime("%a"))  # Weekday, short version
print(x.strftime("%A"))  # Weekday, full version
