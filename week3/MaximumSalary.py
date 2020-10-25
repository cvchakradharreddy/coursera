def is_x_greater(x, y):
    return ((x * (10 ** len(str(y)))) + y) > ((y * (10 ** len(str(x)))) + x)


def get_max_salary():
    max_salary = []

    while len(a) > 0:
        max_index = 0
        for i in range(1, len(a)):
            if is_x_greater(a[i], a[max_index]):
                max_index = i
        max_salary.append(a[max_index])
        a.pop(max_index)

    return max_salary


_ = int(input())
a = [int(x) for x in input().split()]
print(*get_max_salary(), sep='')
