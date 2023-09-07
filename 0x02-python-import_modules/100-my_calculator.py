#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)

    a = int(argv[1])
    b = int(argv[3])
    operators = ["+", "-", "*", "/"]
    from calculator_1 import add, sub, mul, div
    functions = [add, sub, mul, div]
    for i, s in enumerate(operators):
        if argv[2] == s:
            print("{} {} {} = {}".format(a, s, b, functions[i](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
