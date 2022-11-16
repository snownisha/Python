#Exception Handling
a = 5
b = 0
try:
    print(a/b)
except Exception as e:
    print("Dont use 0 because it is ", e)

print("Bye")

