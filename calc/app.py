# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_input():
    a = int(request.args["a"])
    b = int(request.args["b"])
    c = add(a,b)
    return f"<h1>{a} + {b} = {c}</h1>"

@app.route('/sub')
def subtract_input():
    a = int(request.args["a"])
    b = int(request.args["b"])
    c = sub(a,b)
    return f"<h1>{a} - {b} = {c}</h1>"

@app.route('/mult')
def multiply_input():
    a = int(request.args["a"])
    b = int(request.args["b"])
    c = mult(a,b)
    return f"<h1>{a} * {b} = {c}</h1>"

@app.route('/div')
def divide_input():
    a = int(request.args["a"])
    b = int(request.args["b"])
    c = div(a,b)
    return f"<h1>{a} / {b} = {c}</h1>"

@app.route('/math/<operation>')
def all_in_one(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    if operation == "add":
        c = add(a,b)
    if operation == "sub":
        c = sub(a,b)
    if operation == "mult":
        c = mult(a,b)
    if operation == "div":
        c = div(a,b)
    return f"Using {operation}, your answer is {c}!"