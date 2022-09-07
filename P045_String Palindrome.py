#Program to check whether the given string is palindrome or not
String = "ANIMAL"

StringReverse = reversed(String)

if list(String)==list(StringReverse):
    print("Palindrome")
else:
    print("Not Palindrome")
