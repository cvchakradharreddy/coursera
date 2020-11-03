def binary_search(item):
    index = -1
    l, r = 0, len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        if item == a[mid]:
            index = mid
            break
        elif item > a[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return index


def get_binary_search_results():
    return [binary_search(item) for item in b]


a = [int(i) for i in input().split()]
n = a.pop(0)
b = [int(j) for j in input().split()]
k = b.pop(0)
print(*get_binary_search_results())
