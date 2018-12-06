"""
Euler problem 76
Code written by Carolyn Ryan

It is possible to write five as a sum in exactly six different ways:
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""
pos_sums_dict = {}


def possible_sums(num, minimum = 1):
    """
    Recursive solution to euler 76, counts how many different ways we can sum up to a given number
    Uses dictionary to store results we've already calculated to speed up recursion
    :param num: number to sum up to
    :param minimum: number to only count down to, accounts for duplicates
    :return: number of possible sums that add up to num
    """
    # If this has already been calculated, we can take it directly from the dictionary
    if (num, minimum) in pos_sums_dict: # todo CHANGED: in now uses hash instead of linear search!
        return pos_sums_dict[(num,minimum)]

    # If number is 1, we cannot sum up to that without using either a single term or a non-positive integer
    if num <= 1:
        return 0

    sums = 1
    # Only loop over first half, because additions for later half will already be accounted for
    for i in range(1, num//2+1):
        if i >= minimum:
            new_num = num-i
            print("{}+{}".format(new_num, i))
            sums += possible_sums(new_num, i)

    # Add to dictionary so if we need to re-calculate, we can do so faster
    pos_sums_dict[(num, minimum)] = sums
    return sums


if __name__ == '__main__':
    num = 100
    sums = possible_sums(num)
    print(sums)


# def possible_sums(num):
#     """
#     * DOESN'T WORK, FIRST ATTEMPT *
#     Have to account for overlap, this solution takes into account 2+3 as well as 3+2
#     could try to do something with max number to have in addition equations
#     :param num: number to sum up to
#     :return: number of possible sums that add up to num
#     """
#     # If we are looking to how many ways we can write a 1, it can only be written 1 way
#     if num == 1:
#         return 1
#     sums = 1
#     for i in range(num-1, 0, -1):
#         # want to find all the ways you can write num - i
#         # So would find all equations of i + .... = num
#         new_num = num - i
#         sums += possible_sums(new_num)
#
#     return sums
