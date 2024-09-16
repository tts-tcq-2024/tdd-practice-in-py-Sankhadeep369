import re

class NegativeNumberException(Exception):
    def __init__(self, negatives):
        self.negatives = negatives
        super().__init__(f"Negatives not allowed: {', '.join(map(str, negatives))}")

def get_delimiter(numbers):
    if numbers.startswith('//'):
        parts = numbers.split('\n', 1)
        return re.escape(parts[0][2:]), parts[1]  # Custom delimiter
    return ',|\n', numbers  # Default delimiter

def split_numbers(numbers, delimiter):
    return re.split(delimiter, numbers)

def filter_numbers(num_list):
    return [int(n) for n in num_list if n.isdigit()]

def check_for_negatives(numbers):
    negatives = [n for n in numbers if n < 0]
    if negatives:
        raise NegativeNumberException(negatives)

def sum_numbers(numbers):
    return sum(n for n in numbers if n <= 1000)

def add(numbers):
    if not numbers:
        return 0

    delimiter, numbers = get_delimiter(numbers)
    num_list = split_numbers(numbers, delimiter)
    num_list = filter_numbers(num_list)
    
    check_for_negatives(num_list)
    return sum_numbers(num_list)
