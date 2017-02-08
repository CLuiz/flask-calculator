from flask import Flask, jsonify, render_template

app = Flask(__name__)

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

# @app.route('/calc/<operator>/<int:num1>/<int:num2>')
# def add(operator, num1, num2):
#     if operator == 'add':
#         total = num1 + num2
#         return_obj = {
#             'operator': operator,
#             'num1': num1,
#             'num2': num2,
#             'solution': total
#         }
#         return jsonify(return_obj)

if __name__ =='__main__':
    app.run(debug=True)
