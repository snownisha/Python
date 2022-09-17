#Fibonacci Sequence
num1, num2 = 0, 1
print("Fibonacci sequence:")
for i in range(10):
    print(num1, end="  ")
    res = num1 + num2
    num1 = num2
    num2 = res
