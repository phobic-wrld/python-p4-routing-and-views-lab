#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:param>")
def print_string(param):
    print(param)  # print to console
    return param  # return plain text

@app.route("/count/<int:param>")
def count(param):
    output = ""
    for i in range(param):
        output += f"{i}\n"
    return output  # return plain text with newline characters

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)
    else:
        return "Invalid operation"
    return f"{num1} {operation} {num2} = {result}"  # return plain text

if __name__ == "__main__":
    app.run(debug=True)