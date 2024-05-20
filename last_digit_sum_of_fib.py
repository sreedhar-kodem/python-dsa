def last_digit_sum_of_fib(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    fib_sum=previous+current
    for _ in range(n - 1):
        previous, current = current, current+previous
        fib_sum+=current

    return fib_sum%10

if __name__ == '__main__':
    n = int(input())
    print(last_digit_sum_of_fib(n))
