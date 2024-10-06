def loop(range:int) -> int:
    print(range)
    if range == 0: return range
    return loop(range-1)

loop(10)

def condition_loop(start:int, stop:int) -> int:
    print(start)
    if start > stop:
        if start == stop: return start
        return condition_loop(start-1, stop)
    else:
        if start == stop: return start
        return condition_loop(start+1, stop)
    
condition_loop(-1,-10)
condition_loop(-9,0)
    
def factorial(n:int)-> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(f'Factorial 5: {factorial(5)}')

"""
Case factorial(5):

factorial(5)
    └── factorial(4)
            └── factorial(3)
                    └── factorial(2)
                            └── factorial(1)
                                    └── factorial(0) = 1
                            ┌── return 1 * 1 = 1
                    ┌── return 2 * 1 = 2
            ┌── return 3 * 2 = 6
    ┌── return 4 * 6 = 24
┌── return 5 * 24 = 120

"""

def fibonacci(n)-> int:
    if n == 0:  # Caso base 1
        return 0
    elif n == 1:  # Caso base 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Chamada recursiva
    

print(f'Fibonacci 5: {fibonacci(5)}')

"""
Case fibonacci(5):

fibonacci(5)
├── fibonacci(4)
│   ├── fibonacci(3)
│   │   ├── fibonacci(2)
│   │   │   ├── fibonacci(1) = 1
│   │   │   └── fibonacci(0) = 0
│   │   └── fibonacci(1) = 1
│   └── fibonacci(2)
│       ├── fibonacci(1) = 1
│       └── fibonacci(0) = 0
└── fibonacci(3)
    ├── fibonacci(2)
    │   ├── fibonacci(1) = 1
    │   └── fibonacci(0) = 0
    └── fibonacci(1) = 1
"""

def tribonacci(n)-> int:
    if n==0: return 0
    elif n==1: return 1
    elif n==2: return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    
print(f'Tribonacci 4: {tribonacci(4)}')

"""
Case tribonacci(4):

tribonacci(4)
├── tribonacci(3)
│   ├── tribonacci(2)
│   │   ├── tribonacci(1) = 1
│   │   └── tribonacci(0) = 0
│   └── tribonacci(1) = 1
├── tribonacci(2)
│   ├── tribonacci(1) = 1
│   └── tribonacci(0) = 0
└── tribonacci(1) = 1
"""

def sum(n:int) -> int:
    if n == 0: return 0
    return n + sum(n-1)

print(f"Sum of the First 4 Numbers: {sum(4)}")

"""
Case sum(4):

sum(4)
│
├── sum(3)
│   ├── sum(2)
│   │   ├── sum(1)
│   │   │   ├── sum(0)
│   │   │   │   └── return 0
│   │   │   └── return 1 + 0 = 1
│   │   └── return 2 + 1 = 3
│   └── return 3 + 3 = 6
└── return 4 + 6 = 10

"""

def merge_search(array, start, end, target):
    # Stop condition: if the list has no more elements
    if start > end:
        return -1  # Not found
    
    middle = (start + end) // 2  # calculates the middle of the list
    
    # Checks if the central element is the target
    if array[middle] == target:
        return middle  # Index of found element
    # If the target is smaller, search in the left half
    elif array[middle] > target:
        return merge_search(array, start, middle - 1, target)
    # If the target is bigger, search in the right half
    else:
        return merge_search(array, middle + 1, end, target)

# Example:
ordered_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = merge_search(ordered_array, 0, len(ordered_array) - 1, target)

if result != -1:
    print(f"Element 7 found in index {result}")
else:
    print("Element not found")
