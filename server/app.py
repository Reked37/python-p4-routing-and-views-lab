#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
      print(parameter)
      return parameter

@app.route('/count/<int:parameter>')
def count_numbers(parameter):
    numbers= '\n'.join(str(i) for i in range(parameter))
    return numbers

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math_operation(num1, operation, num2):
    if operation == '+':
        total =num1 + num2
    elif operation == '-':
        total = num1 - num2
    elif operation == '*':
        total = num1 * num2
    elif operation == '/' or operation == 'div':
        total = num1 / num2
    elif operation == '%':
        total = num1 % num2
    return str(total)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
