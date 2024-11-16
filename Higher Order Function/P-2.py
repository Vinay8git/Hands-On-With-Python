def summation(nums):
    return sum(nums)


def main(f, args):
    result = f(args)
    print(result)
    print("Inside Function" + str(f))


if __name__ == "__main__":
    main(summation, [1, 2, 3, 4])
    print(summation)
