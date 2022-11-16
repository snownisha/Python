#Operator Overloading
class stud:

    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def add(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = stud(m1,m2)

        return s3


s1 = stud(99,78)
s2 = stud(100,23)


s3 = s1 + s2
print(s3.m1)