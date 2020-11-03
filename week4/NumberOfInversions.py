def get_number_of_inversions(a):
    if len(a) < 2:
        return a, 0
    else:
        mid = len(a) // 2
        l = a[:mid]
        r = a[mid:]
        left, left_count = get_number_of_inversions(l)
        right, right_count = get_number_of_inversions(r)
        left_copy = left.copy()
        right_copy = right.copy()
        values = []
        merge_count = 0
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                values.append(left[0])
                left.pop(0)
            else:
                values.append(right[0])
                right.pop(0)
        if len(left) > 0:
            values.extend(left)
        if len(right) > 0:
            values.extend(right)

        while len(left_copy) > 0 and len(right_copy) > 0:
            if left_copy[0] <= right_copy[0]:
                left_copy.pop(0)
            else:
                merge_count += (len(left_copy) * 1)
                right_copy.pop(0)

        return values, left_count + right_count + merge_count


def number_of_inversion(a):
    return get_number_of_inversions(a)[1]


if __name__ == "__main__":
    _ = int(input())
    a = [int(x) for x in input().split()]
    print(number_of_inversion(a))
