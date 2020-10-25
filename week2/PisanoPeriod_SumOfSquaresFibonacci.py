def get_pisano_period(m):
    previous_fib, current_fib = 0, 1
    previous_sum, current_sum = 0, 1
    previous, current = 0, 1
    for i in range(2, (m * m) + 1):
        previous_fib, current_fib = current_fib, (previous_fib + current_fib) % 10
        previous_sum, current_sum = current_sum, (current_sum + (current_fib ** 2)) % 10
        if (previous_sum % m, current_sum % m) == (0, 1):
            return i - 1


if __name__ == '__main__':
    print(get_pisano_period(int(input())))
