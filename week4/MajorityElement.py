def get_majority(a):
    if len(a) > 1:
        mid = len(a) // 2
        l = a[:mid]
        r = a[mid:]
        left_majority_elm, left_majority_count = get_majority(l)
        right_majority_elm, right_majority_count = get_majority(r)
        if left_majority_elm != -1:
            for elm in r:
                if elm == left_majority_elm:
                    left_majority_count += 1
        if right_majority_elm != -1:
            for elm in l:
                if elm == right_majority_elm:
                    right_majority_count += 1
        if left_majority_count > len(a) / 2:
            return left_majority_elm, left_majority_count
        elif right_majority_count > len(a) / 2:
            return right_majority_elm, right_majority_count
        else:
            return -1, 0
    else:
        return a[0], 1


_ = int(input())
a = [int(x) for x in input().split()]
x = 1 if get_majority(a)[1] > 0 else 0
print(x)
