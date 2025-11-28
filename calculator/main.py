# Simple calculator

import sys
from pkg.calculator import Calculator
from pkg.render import format_json_output


def main():
    calculator = Calculator()
    
    try:
        with open('args.txt', 'r') as f:
            expression = f.read()
    except FileNotFoundError:
        print("Error: args.txt not found.")
        return

    if not expression:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    try:
        result = calculator.evaluate(expression)
        if result is not None:
            print(f"Result before formatting: {result}")
            to_print = format_json_output(expression, result)
            print(to_print)
        else:
            print("Error: Expression is empty or contains only whitespace.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()