def custom_merge_sort_desc(l):
    if len(l) < 2:
        return l
    else:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        left_sorted = custom_merge_sort_desc(left)
        right_sorted = custom_merge_sort_desc(right)
        values = []
        while len(left_sorted) > 0 and len(right_sorted) > 0:
            if (left_sorted[0][0] / left_sorted[0][1]) > (right_sorted[0][0] / right_sorted[0][1]):
                values.append(left_sorted[0])
                left_sorted.pop(0)
            else:
                values.append(right_sorted[0])
                right_sorted.pop(0)
        if len(left_sorted) > 0:
            values.extend(left_sorted)
        if len(right_sorted) > 0:
            values.extend(right_sorted)
        return values


def get_max_value_loot(loot, w):
    sorted_loot = custom_merge_sort_desc(loot)
    max_value = 0
    for i in sorted_loot:
        if w > i[1]:
            max_value += i[0]
            w -= i[1]
        elif w > 0:
            max_value += w * (i[0] / i[1])
            break
        else:
            break
    return round(max_value, 4)


if __name__ == '__main__':
    n, w = map(int, input().split())
    loot = [[int(i) for i in input().split()] for _ in range(n)]
    print(get_max_value_loot(loot, w))
