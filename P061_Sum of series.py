#Program to print the sum of seri
x = 6
ser= 2
sum = 0

for i in range(0, x):
    print(ser, end="+")
    sum+= ser
    start = ser * 10 + 2
print("\n Sum of above series is:", sum)
