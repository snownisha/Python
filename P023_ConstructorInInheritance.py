#Constructor in Inheritance
class A:

    def __init__(self):
        print ("in A init")

    def feature1(self):
        print("Feature1 is working")

    def feature2(self):
        print("Feature2 is working")


class B(A):
    def __init__(self):
        print ("in B init")

    def feature3(self):
        print("Feature3 is working")

    def feature4(self):
        print("Feature4 is working")

class C(B):
    def __init__(self):
        print ("in C init")

    def feature5(self):
        super().feature2()
        print("Feature5 is working")

a1= A()
b1= B()
c1 = C()