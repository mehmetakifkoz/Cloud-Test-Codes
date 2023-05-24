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

def main():
    num = int(input("Enter a number to calculate its factorial: "))
    factorial = calculate_factorial(num)
    print("Factorial of", num, "is", factorial)

    fib_num = int(input("Enter the number of Fibonacci sequence terms to generate: "))
    fibonacci_seq = fibonacci_sequence(fib_num)
    print("Fibonacci sequence:", fibonacci_seq)

if __name__ == "__main__":
    main()
