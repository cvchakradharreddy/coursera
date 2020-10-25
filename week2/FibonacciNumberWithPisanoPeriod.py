def get_fb_mod(n, m):
    p = get_pisano_period(m)
    r = n % p
    previous, current = 0, 1
    if r == 0:
        return previous
    elif r == 1:
        return current
    else:
        for i in range(2, r + 1):
            previous, current = current, (previous + current) % m
        return current


def get_pisano_period(m):
    previous, current = 0, 1
    for i in range(2, (m * m) + 1):
        previous, current = current, (previous + current) % m
        if (previous, current) == (0, 1):
            return i - 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fb_mod(n, m))
