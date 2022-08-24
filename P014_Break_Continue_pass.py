#Break
av = 5
x= int(input("How many cookies you want? :"))

i =1
while i <= x:

    if i>av:
        break

    print('Cookies')
    i+=1

print('Bye')


#continue
for i in range (1,10):
    if i%3 ==0:
        continue
    print(i)

#pass
for i in range (1,10):
    if i%3 ==0:
        pass
    print(i)