import re

class NegativeNumberException(Exception):
    def __init__(self, negatives):
        self.negatives = negatives
        super().__init__(f"Negatives not allowed: {', '.join(map(str, negatives))}")

def add(numbers):
    if not numbers:
        return 0

    delimiter = ',|\n'
    
    # Check for custom delimiter
    if numbers.startswith('//'):
        parts = numbers.split('\n', 1)
        delimiter = re.escape(parts[0][2:])
        numbers = parts[1]
    
    # Split the numbers by the determined delimiter(s)
    num_list = re.split(delimiter, numbers)
    
    # Convert to integers, filter out large numbers and find negatives
    num_list = [int(n) for n in num_list if n.isdigit()]
    negatives = [n for n in num_list if n < 0]
    
    # Throw exception if there are any negatives
    if negatives:
        raise NegativeNumberException(negatives)
    
    # Sum numbers less than or equal to 1000
    return sum(n for n in num_list if n <= 1000)

