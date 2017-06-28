from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/calc')
def calc():
    # connection
    with sqlite3.connect('calc.db') as connection:
        # create cursor
        c = connection.cursor()
        # execute sql statement
        c.execute("""SELECT * FROM calculations""")
        rows = c.fetchall()
        # iterate through returned rows
            # create some sort of container
        # return data
    return 'test'

@app.route('/calc/<operator>/<int:num1>/<int:num2>')
def add(operator, num1, num2):
    if operator == 'add':
        total = num1 + num2
    if operator == 'sub':
        total = num1 - num2
    if operator == 'mult':
        total = num1 * num2
    if operator == 'div':
        total = num1 / num2
    data = {
            'operator': operator,
            'num1': num1,
            'num2': num2,
            'solution': total
            }
    return render_template('index.html', data=data)

if __name__ =='__main__':
    app.run(debug=True)
