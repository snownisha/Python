#Comparing Objects in Python
class computer:
    def __init__(self):
        self.name = "Snow"
        self.age = 24


    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = computer()
c1.age= 100
c2 = computer()

if c1.compare(c2):
    print("They are same")
else:
    print("Not Same")

c1.name = "Nisha"


print(c1.name)
print(c1.age)
print(c2.age)
print(c2.name)