class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")#

class Laptop:

    def code(self, ide):
        ide.execute()

ide = PyCharm()

lap1 = Laptop()
lap1.code(ide)