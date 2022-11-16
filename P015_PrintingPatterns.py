#Printing Patterns in Python
for i in range (4):
    for j in range (4):
        print('# ', end="")
    print()

for i in range (5):
    for j in range (i):
        print('# ', end="")
    print()


print()
for i in range (4):
    for j in range(4-i):
        print('# ', end="")
    print()