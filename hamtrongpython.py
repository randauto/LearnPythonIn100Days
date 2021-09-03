# cach khai bao ham trong python

'''
def functionName(list of parameter)
        code detailing what the function should do
        return [expression]

'''


def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if numberToCheck % x == 0:
            return False
    return True


myNumber = 17

print("Number ", myNumber, "is prime? : ", checkIfPrime(myNumber))
