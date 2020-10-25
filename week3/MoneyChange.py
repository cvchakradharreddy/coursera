def get_minimum_coins_change(n):
    no_of_coins = 0
    while n > 0:
        if n >= 10:
            n -= 10
        elif n >= 5:
            n -= 5
        else:
            n -= 1
        no_of_coins += 1
    return no_of_coins


if __name__ == '__main__':
    print(get_minimum_coins_change(int(input())))
