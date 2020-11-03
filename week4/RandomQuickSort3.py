import random


def swap(a, x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp


def get_quick_sorted3(a, l, r):
    if l < r:
        pivot_index = random.randint(l, r)
        swap(a, l, pivot_index)
        pivot = a[l]
        j = k = l
        for i in range(l + 1, r + 1):
            if a[i] < pivot:
                if i - j > 1:
                    swap(a, i, j + 1)
                    if k - j > 0:
                        swap(a, i, k + 1)
                j += 1
                k += 1
            elif a[i] == pivot:
                if i - k > 1:
                    swap(a, i, k + 1)
                k += 1
        swap(a, l, j)
        get_quick_sorted3(a, l, j - 1)
        get_quick_sorted3(a, k + 1, r)


def random_quick_sort3(a):
    get_quick_sorted3(a, 0, len(a) - 1)


if __name__ == '__main__':
    _ = int(input())
    a = [int(x) for x in input().split()]
    random_quick_sort3(a)
    print(*a)
