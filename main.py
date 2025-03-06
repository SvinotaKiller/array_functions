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