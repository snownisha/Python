pos = -1
def search (list,n):
    l = 0
    u = len(list)-1

    while l <=u:
        mid = (l+u)//2

        if list[mid]== n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid]<n:
                l= mid
            else:
                u = mid


list = [1,2,3,4,5]
n = 5

if search (list ,n):
    print("It is there in the list")
else:
    print("It is not there in the list")