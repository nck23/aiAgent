from pkg.calculator import Calculator
from pkg.render import format_json_output

calculator = Calculator()
expression = "3 + 5"
result = calculator.evaluate(expression)
print(format_json_output(expression, result))