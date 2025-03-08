import concurrent.futures
import time

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def calculate_fibonacci_numbers(numbers):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(fibonacci, numbers)
    return list(results)

if __name__ == "__main__":
    numbers = [30, 32, 34, 36]
    start_time = time.time()
    results = calculate_fibonacci_numbers(numbers)
    end_time = time.time()
    
    for num, result in zip(numbers, results):
        print(f"Fibonacci({num}) = {result}")
    
    print(f"Time taken: {end_time - start_time:.2f} seconds")
