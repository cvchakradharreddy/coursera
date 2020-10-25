def get_gcd(x, y):
    if x > y:
        temp = x
        x = y
        y = temp
    remainder = y % x
    if remainder == 0:
        return x
    else:
        return get_gcd(remainder, x)


def get_lcm(x, y):
    if x > y:
        temp = x
        x = y
        y = temp
    return (y // get_gcd(x, y)) * x


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_lcm(a, b))
