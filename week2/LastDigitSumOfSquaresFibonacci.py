def get_last_digit_sum_fib(n):
    previous_fib, current_fib = 0, 1
    previous_sum, current_sum = 0, 1
    #To get last digit use Fn mod 10 with pisano period 30
    r = n % 30
    if r == 0:
        return previous_sum
    elif r == 1:
        return current_sum
    else:
        for i in range(2, r + 1):
            previous_fib, current_fib = current_fib, (previous_fib + current_fib) % 10
            previous_sum, current_sum = current_sum, (current_sum + current_fib ** 2) % 10
        return current_sum


if __name__ == '__main__':
    print(get_last_digit_sum_fib(int(input())))
