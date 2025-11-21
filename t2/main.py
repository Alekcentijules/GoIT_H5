from typing import Callable, Generator
import re

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Generates real numbers from text.
    
    Args:
        text (str): Text with numbers such as 123.45
    
    Yields:
        float: Found numbers
    """
    pattern = r" \d+\.\d+ "
    for num in re.findall(pattern, text):
        yield float(num)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Calculates the total income from the text using a generator.

    Args:
        text (str): Input text.
        func (Callable): Generator function that returns float.

    Returns:
        float: The sum of all numbers.
    """
    return sum(func(text)) if text.strip() else 0.0

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими " \
       "надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
