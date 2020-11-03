import random


def is_less(x, y):
    less = False
    if x[0] < y[0]:
        less = True
    elif x[0] == y[0]:
        less = x[1] < y[1]
    return less


def is_equal(x, y):
    return x[0] == y[0] and x[1] == y[1]


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
            elif is_equal(a[i], pivot):
                if i - k > 1:
                    swap(a, i, k + 1)
                k += 1
        swap(a, l, j)
        get_quick_sorted3(a, l, j - 1)
        get_quick_sorted3(a, k + 1, r)


def random_quick_sort3(a):
    get_quick_sorted3(a, 0, len(a) - 1)


def get_matching_segments(x, S):
    matching_segments = 0
    l = 0
    r = len(S) - 1
    while l <= r:
        mid = (l + r) // 2
        if S[mid][0] == x:
            pass
        elif S[mid][0] < x:
            l = mid + 1
        else:
            r = mid - 1
    return matching_segments


def get_number_of_segments(A, B, P):
    all_points_flat = []
    all_points_flat.extend([[int(a), 1] for a in A])  # Left Boundary = 1
    all_points_flat.extend([[int(b), 3] for b in B])  # Right Boundary = 3
    all_points_flat.extend([[int(p), 2] for p in P])  # Point = 2
    random_quick_sort3(all_points_flat)
    count_points = {}
    count = 0
    for p in all_points_flat:
        if p[1] == 1:  # Left Boundary
            count += 1
        elif p[1] == 3:  # Right Boundary
            count -= 1
        else:  # Point
            count_points[p[0]] = count

    return [count_points[p] for p in P]


s, p = map(int, input().split())
A = []
B = []
for _ in range(s):
    x = input().split()
    A.append(x[0])
    B.append(x[1])

P = [int(x) for x in input().split()]
print(*get_number_of_segments(A, B, P))
