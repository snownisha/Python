#Method Overridding
class a:

    def show(self):
        print("in A show")

class b(a):
        pass

a1 = b()
a1.show()