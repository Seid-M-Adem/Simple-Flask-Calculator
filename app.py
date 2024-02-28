#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        x = float(request.form['x'])
        y = float(request.form['y'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = x + y
            operator = '+'
        elif operation == 'subtract':
            result = x - y
            operator = '-'
        elif operation == 'multiply':
            result = x * y
            operator = 'x'
        elif operation == 'divide':
            if y == 0:
                return render_template('index.html', error='Division by zero')
            result = x / y
            operator = '/'
        
        return render_template('index.html', result=result, operator=operator, x=x, y=y)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
