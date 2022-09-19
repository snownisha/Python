#Program to print Prime Numbers
start = 20
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                break
        else:
            print(num)
