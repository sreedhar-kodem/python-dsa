def last_digit_partial_sum(n,m):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n):
        previous, current = current, current+previous
    fib_sum=previous
    for _ in range(n,m+1):
        previous, current = current, current+previous
        fib_sum+=current

    return fib_sum
if __name__ == '__main__':
    n,m = map(int,input().split())
    print(last_digit_partial_sum(n,m))