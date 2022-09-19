n = 5
start = 2
sum = 0

for i in range(0, n):
    print(start, end="+")
    sum+= start
    start = start * 10 + 2
print("\n Sum of above series is:", sum)