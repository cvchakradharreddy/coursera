def get_last_digit_sum_fib_partial(m, n):
    previous_fib, current_fib = 0, 1
    previous_sum, current_sum = 0, 1
    # To get last digit use Fn mod 10 with pisano period 60
    if m == 0:
        pisano_partial_start_before = 0
    else:
        pisano_partial_start_before = (m - 1) % 60
    pisano_partial_end = n % 60

    partial_start_before_sum_last = pisano_partial_start_before
    partial_end_sum_last = pisano_partial_end

    for i in range(2, max(pisano_partial_start_before, pisano_partial_end) + 1):
        previous_fib, current_fib = current_fib, (previous_fib + current_fib) % 10
        previous_sum, current_sum = current_sum, (current_sum + current_fib) % 10
        if i == pisano_partial_start_before:
            partial_start_before_sum_last = current_sum
        elif i == pisano_partial_end:
            partial_end_sum_last = current_sum
    last_digit = partial_end_sum_last - partial_start_before_sum_last
    if last_digit < 0:
        return 10 + last_digit
    else:
        return last_digit


if __name__ == '__main__':
    m, n = map(int, input().split())
    print(get_last_digit_sum_fib_partial(m, n))
