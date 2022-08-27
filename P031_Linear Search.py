
def search(list,n):
    i=0
    while i< len(list):
        if list[i] ==n:
            pos = i
            return True
        i= i+1



list = [1,2,3,4,5]
n = 5

if search (list,n):
    print("It is there in the list")
else:
    print("It is not there in the list")