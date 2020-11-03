# time complexity = O(nlogn)

import math
from operator import itemgetter


def get_distance(p1, p2):
    return math.pow(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2), 0.5)


def get_min_distance(Px, Py):
    if len(Px) < 2:
        return math.inf
    elif len(Px) == 2:
        return get_distance(Px[0], Px[1])
    else:
        mid = len(Px) // 2
        Px_left = Px[:mid]
        Px_right = Px[mid + 1:]
        pivot = Px[mid]
        dl = get_min_distance(Px_left, Py)
        dr = get_min_distance(Px_right, Py)
        d = min(dl, dr)
        Py_partition = []
        for p in Py:
            if abs(pivot[0] - p[0]) <= d:
                Py_partition.append(p)
        for i in range(len(Py_partition) - 1):
            j = i + 1
            while j - i <= 7 and j < len(Py_partition):
                d = min(d, get_distance(Py_partition[i], Py_partition[j]))
                j += 1
        return d


def get_closest_distance(P):
    Px = sorted(P, key=itemgetter(0))
    Py = sorted(P, key=itemgetter(1))
    return get_min_distance(Px, Py)


if __name__ == "__main__":
    n = int(input())
    P = [[int(p) for p in input().split()] for _ in range(n)]
    print("{0:.9f}".format(get_closest_distance(P)))
