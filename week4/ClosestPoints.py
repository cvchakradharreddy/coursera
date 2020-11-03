# time complexity = O(n(logn)^2)

import math


def get_distance(p1, p2):
    return math.pow(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2), 0.5)


def get_min_distance(Px):
    if len(Px) < 2:
        return math.inf
    elif len(Px) == 2:
        return get_distance(Px[0], Px[1])
    else:
        mid = len(Px) // 2
        left = Px[:mid]
        right = Px[mid + 1:]
        pivot = Px[mid]
        dl = get_min_distance(left)
        dr = get_min_distance(right)
        d = min(dl, dr)
        Px_partition = []
        for p in Px:
            if abs(pivot[0] - p[0]) <= d:
                Px_partition.append(p)
        Px_partition.sort(key=lambda p: p[1])
        for i in range(len(Px_partition) - 1):
            j = i + 1
            while j - i <= 7 and j < len(Px_partition):
                d = min(d, get_distance(Px_partition[i], Px_partition[j]))
                j += 1
        return d


def get_closest_distance(P):
    Px = sorted(P, key=lambda p: p[0])
    return get_min_distance(Px)


if __name__ == "__main__":
    n = int(input())
    P = [[int(p) for p in input().split()] for _ in range(n)]
    print("{0:.9f}".format(get_closest_distance(P)))
