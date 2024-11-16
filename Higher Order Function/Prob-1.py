def add_two_nums(x, y):
    return x + y


def add_three_nums(x, y, z):
    return x + y + z


def get_appropriate_function(num_len):
    if num_len == 3:
        return add_three_nums
    else:
        return add_two_nums


if __name__ == "__main__":
    args = [1, 2, 3]
    num_len = len(args)
    res_function = get_appropriate_function(num_len)
    print(res_function)
    print(res_function(*args))
    args = [1, 2]
    num_len = len(args)
    res_function = get_appropriate_function(num_len)
    print(res_function)
    print(res_function(*args))
