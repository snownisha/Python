class student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        return (s1.name, s1.rollno)

    class laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'


s1 = student('Nisha', 189294)
s2 = student('Snow', 189094)

lap1 = student.laptop()
lap2 = student.laptop()

print(id(lap1))
print("Roll Number is: " + str(s1.rollno))
print(s1.show())

