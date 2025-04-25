def generate_fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    while len(fibonacci_series) < n:
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series


n = 10
fibonacci_series = generate_fibonacci(n)
print(f"First {n} numbers in the Fibonacci series: {fibonacci_series}")

