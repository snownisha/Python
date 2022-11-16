#Instance and Class Variable
class subjects:
    TotalMarks = 100

    def __init__(self):
        self.lang = 'English'
        self.location = 'Germany'



adsp = subjects()
acc = subjects()
ubiq = subjects()

acc.TotalMarks= 90
subjects.TotalMarks = 50

print (adsp.lang, acc.TotalMarks, ubiq.TotalMarks)