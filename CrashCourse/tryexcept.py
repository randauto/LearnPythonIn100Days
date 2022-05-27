x = -1
try:
    print(100 / 0)
except ZeroDivisionError:
    print("Divide by zero")
except:
    print("Have some error occur")
finally:
    print("This line must show")

    if x < 0:
        raise Exception("Sorry, no numbers below zero")
