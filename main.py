arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_greater(arr, vaule):

    new_arr = []

    for number in arr:
        if number > vaule:
            new_arr.append(number)

    return new_arr

print(filter_greater(arr, 5))