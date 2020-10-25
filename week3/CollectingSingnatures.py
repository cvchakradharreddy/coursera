def get_min_common_points():
    segments.sort(key=lambda x: x[0])
    covered = [segments[0]]
    segments.pop(0)
    while len(segments) > 0:
        not_found = True
        a = segments[0][0]
        b = segments[0][1]
        for j in range(len(covered)):
            covered_a = covered[j][0]
            covered_b = covered[j][1]
            common = [max(a, covered_a), min(b, covered_b)]
            if common[1] - common[0] >= 0:
                covered.pop(j)
                segments.pop(0)
                covered.append(common)
                not_found = False
                break
        if not_found:
            segments.pop(0)
            covered.append([a, b])

    common_points = {c[1] for c in covered}
    return common_points


n = int(input())
segments = [[int(x) for x in input().split()] for _ in range(n)]
x = get_min_common_points()
print(len(x))
print(*x)
