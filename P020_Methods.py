#Method in Python
class student:
    school = 'Offenburg University'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class")


s1 = student(23,45,67)
s2 = student(98,56,43)

print(s1.m3)
print(s1.avg())
print(student.getschool())

student.info()