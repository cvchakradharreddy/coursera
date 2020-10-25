def get_min_refills(m):
    stops.append(d)
    can_cover = m
    last_stop = 0
    min_refills = 0
    i = 0
    while i < len(stops):
        if stops[i] < can_cover:
            i += 1
        elif stops[i] == can_cover:
            if i == len(stops) - 1:
                break
            else:
                min_refills += 1
                can_cover = stops[i] + m
                last_stop = i
                i += 1
        else:
            if last_stop == i - 1:
                min_refills = -1
                break
            else:
                min_refills += 1
                can_cover = stops[i-1] + m
                last_stop = i - 1

    return min_refills


if __name__ == '__main__':
    d = int(input())
    m = int(input())
    _ = int(input())
    stops = [int(x) for x in input().split()]
    print(get_min_refills(m))
