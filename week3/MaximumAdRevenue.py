def get_max_ad_revenue():
    a.sort(reverse=True)
    b.sort(reverse=True)
    max_revenue = 0
    for i in range(len(a)):
        max_revenue += a[i] * b[i]
    return max_revenue


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(get_max_ad_revenue())
