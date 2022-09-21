#Reverse Number
num = 1234567
reverse_num = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_num = (reverse_num * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_num)
