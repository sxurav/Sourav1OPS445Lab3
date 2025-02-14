#!/usr/bin/env python3

# Author ID: sourav1

def operate(number1, number2, operator):
    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    print(operate(10, 5, 'add'))        # Should print 15
    print(operate(10, 5, 'subtract'))   # Should print 5
    print(operate(10, 5, 'multiply'))   # Should print 50
    print(operate(10, 5, 'divide'))     # Should print error message
