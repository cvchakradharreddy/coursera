def swap(a, x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp


def get_quick_sorted(a, l, r):
    if l < r:
        pivot = a[l]
        j = l
        for i in range(l + 1, r + 1):
            if a[i] <= pivot:
                if i - j > 1:
                    swap(a, i, j + 1)
                j += 1
        swap(a, l, j)
        get_quick_sorted(a, l, j - 1)
        get_quick_sorted(a, j + 1, r)


n = int(input())
a = [int(x) for x in input().split()]
get_quick_sorted(a, 0, n - 1)
print(*a)
