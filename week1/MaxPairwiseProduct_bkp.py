size = int(input())
numbers = [int(x) for x in input().split()]


def get_max_pairwise_product():
    max_one_ind = 0
    max_two_ind = 0
    max_one = 0
    max_two = 0
    for i in range(0, size):
        if numbers[i] > max_one:
            max_one = numbers[i]
            max_one_ind = i

    for i in range(0, size):
        if numbers[i] > max_two and i != max_one_ind:
            max_two = numbers[i]
            max_two_ind = i

    return numbers[max_one_ind] * numbers[max_two_ind]


print(get_max_pairwise_product())
