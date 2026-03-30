"""
Fibonacci number and series algorithms
"""
def fibonacci_next_number(n):
    if n == 0:
        return 0

    if n == 1:
       return 1

    return fibonacci_next_number(n - 1) + fibonacci_next_number(n - 2)

number = 7

print(f"The next Fibonacci number after {number} is {fibonacci_next_number(number)}")

def fibonacci_series(n):
    series = []
    a = 1
    b = 2

    for i in range(n):
        series.append(a)

        next = a + b

        a = b
        b = next

    return series

print("Fibonacci series: ", *fibonacci_series(10), sep=", ")
