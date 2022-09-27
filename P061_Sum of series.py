#Program to find the Sum of series in 
a = 6
ser= 2
sum = 0

for i in range(0, a):
    print(ser, end="+")
    sum+= ser
    start = ser * 10 + 2
print("\n Sum of above series is:", sum)
