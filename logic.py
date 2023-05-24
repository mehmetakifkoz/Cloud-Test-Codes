def calculate_factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * calculate_factorial(n - 1)

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[i - 1] + sequence[i - 2])
        return sequence

def calculate_factorial_and_fibonacci(num, fib_num):
    factorial = calculate_factorial(num)
    fibonacci_seq = fibonacci_sequence(fib_num)

    result = {
        'factorial': factorial,
        'fibonacci_sequence': fibonacci_seq
    }

    return result
