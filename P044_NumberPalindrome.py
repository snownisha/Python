#Number Palindrome
num = input("Enter the number: ")
reverse = int(str(num)[::-1])
if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")