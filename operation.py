print("Welcome to the tip calculator.")
totalBill = input("What was the total bill? $")
percentTip = input("What percentage tip would you like to give? 10, 12, or 15? ")
numberPeople = input("How many people to split the bill? ")
eachPerson = (float(totalBill) + float(totalBill) * (int(percentTip) / 100)) / 7
final_amount = "{:.2f}".format(eachPerson)
print(f"Each person should pay: ${final_amount}")
