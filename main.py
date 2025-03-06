def filter_greater(arr, vaule):

    new_arr = []

    for number in arr:
        if number > vaule:
            new_arr.append(number)

    return new_arr

def filter_less(arr, vaule):

    new_arr = []

    for number in arr:
        if number < vaule:
            new_arr.append(number)

    return new_arr

def filter_equal(arr, vaule):

    new_arr = []

    for number in arr:
        if number == vaule:
            new_arr.append(number)

    return new_arr

def filter_not_equal(arr, vaule):

    new_arr = []

    for number in arr:
        if number != vaule:
            new_arr.append(number)

    return new_arr

def test():

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(filter_greater(arr, 5))
    print(filter_less(arr, 5))
    print(filter_equal(arr, 5))
    print(filter_not_equal(arr, 5))

print(test())