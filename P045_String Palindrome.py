#String Palindrome in python
String = "ANIMAL"

StringReverse = reversed(String)

if list(String)==list(StringReverse):
    print("Palindrome")
else:
    print("Not Palindrome")
