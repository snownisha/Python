#Creating new list in python
def Merge(List1, List2):
    result_list = []

    # iterate first list
    for num in List1:
        if num % 2 != 0:
            result_list.append(num)

    for num in List2:
        if num % 2 == 0:
            result_list.append(num)
    return result_list


List1 = [10, 20, 25, 30, 35]
List2 = [40, 45, 60, 75, 90]
print("result list:", Merge(List1, List2))
