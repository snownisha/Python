# Sum of Current & Previous Number
# I am referring PYnative Python Programming website for practice from P037 to P062
previous_num = 0

for i in range(1, 11):
    sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", previous_num + i)
    previous_num = i
