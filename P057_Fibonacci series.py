#Fibonacci Sequence
num1, num2 = 0, 1
print("Fibonacci sequence:")
for i in range(10):
    # print next number of a series
    print(num1, end="  ")
    # add last two numbers to get next number
    res = num1 + num2
    num1 = num2
    num2 = res
