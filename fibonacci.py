def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')        
        a, b = b, a+b
    print("fib1")
    
def fib2(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')        
        a, b = b, a+b
    print("fib2")