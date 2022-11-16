#Init Method in Python
class city:
    def __init__(self, city, district):
        self.city = city
        self.district = district



    def speci(self):
        print(self.city, self.district)


city1 = city('Chennai', 'Chennai')
city2 = city('Palakurichy', 'Trichy')

city1.speci()
city2.speci()




