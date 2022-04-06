import sys


def divide_two_numbers(n1: int, n2: int) -> None:
    """Divides two numbers"""
    try:
        print(f'Output: {n1 / n2}')
    except ZeroDivisionError:
        print('Cannot divide by zero!', file=sys.stderr)
        pass


if __name__ == '__main__':
    ht = {1: 'st', 2: 'nd'}

    n1, n2 = [int(input(f'Enter {i}{ht.get(i)} digit:\n> ')) for i in range(1, 3)]
    divide_two_numbers(n1, n2)
