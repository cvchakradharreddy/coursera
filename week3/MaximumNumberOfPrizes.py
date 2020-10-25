def get_max_num_prizes():
    sum = 0
    K = []
    if n == 1:
        K.append(1)
    elif n == 2:
        K.append(2)
    else:
        for i in range(1, n):
            sum += i
            if sum == n:
                K.append(i)
                break
            elif sum < n:
                K.append(i)
            else:
                last = K.pop()
                K.append(last + (n - (sum - i)))
                break
    return K


n = int(input())
x = get_max_num_prizes()
print(len(x))
print(*x)
