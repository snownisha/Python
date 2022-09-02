
def number(list):
    FirstNum = list[0]
    LastNum = list[-1]

    if FirstNum == LastNum :
        return True
    else:
        return False

numbX = [10, 20, 30, 40, 10]
print(number(numbX))
numbY = [75, 20, 30, 40, 10]
print(number(numbY))