p=open('Text', 'r')
w1=open('Text', 'w')
w1.write("Cme is my course of study ")

w=open('cme', 'w')
w.write("Cme is my course of study ")

w.write("& Its fun to learn python")

for data in Text:
    w.write(data)
