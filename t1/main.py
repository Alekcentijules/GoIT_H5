from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """
    Returns a function for calculating Fibonacci numbers with caching.
    
    Returns:
        Callable[[int], int]: Function fibonacci(n)
    """
    cache: dict[int, int] = {}
    def fibonacci(n: int) -> int:
        """
        Calculates the nth Fibonacci number using cache.

        Args:Ы
            n (int): Number in the sequence.

        Returns:
            int: nth Fibonacci number.
        """
        nonlocal cache
        if n <= 0: 
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

fibon = caching_fibonacci()
print(fibon(10))