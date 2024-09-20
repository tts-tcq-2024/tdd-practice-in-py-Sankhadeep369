import re

class NegativeNumberException(Exception):
    def __init__(self, negatives):
        self.negatives = negatives
        super().__init__(f"Negatives not allowed: {', '.join(map(str, negatives))}")

def get_delimiter(numbers):
    if numbers.startswith('//'):
        match = re.match(r'//(\[.*\])\n(.*)', numbers)
        if match:
            delimiters = re.findall(r'\[(.*?)\]', match.group(1))
            delimiter_pattern = '|'.join(map(re.escape, delimiters))
            return delimiter_pattern, match.group(2)
        else:
            return re.escape(numbers[2]), numbers.split('\n', 1)[1]
    return ',|\n', numbers

def split_numbers(numbers, delimiter):
    return re.split(delimiter, numbers)

def filter_numbers(num_list):
    return [int(n) for n in num_list if n]

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
