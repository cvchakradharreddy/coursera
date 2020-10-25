def get_fib_num_last_digit(n):
    previous, current = 0, 1
    if n == 0:
        return previous
    elif n > 0:
        for i in range(n - 1):
            previous, current = current, (previous + current) % 10
        return current


if __name__ == '__main__':
    print(get_fib_num_last_digit(int(input())))
