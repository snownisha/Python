class Human:
    def eyes(self):
        print("I can see the world")

    def face(self):
        print("I have a beautiful face")
        self.eyes()

class Female (Human):
    def working(self):
        print("Currently student")

Nisha = Female()
Nisha.face()