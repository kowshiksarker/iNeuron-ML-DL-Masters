import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        operation = request.form['operation']
        num1 = request.form['num1']
        num2 = request.form['num2']
        if(operation=='add'):
            try:
                r = int(num1) + int(num2)
                result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            except ValueError as e:
                result = 'ValueError Occurs:' + str(e) + '.  ' + 'Please input correct value and try again'

        if (operation == 'subtract'):
            try:
                r = int(num1) - int(num2)
                result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            except ValueError as e:
                result = 'ValueError Occurs:' + str(e) + '.  ' + 'Please input correct value and try again'

        if (operation == 'multiply'):
            try:
                r = int(num1) * int(num2)
                result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            except ValueError as e:
                result = 'ValueError Occurs:' + str(e) + '.  ' + 'Please input correct value and try again'

        if (operation == 'divide'):
            try:
                r = int(num1) / int(num2)
                result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            except ValueError as e:
                result = 'ValueError Occurs:' + str(e) + '.  ' + 'Please input correct value and try again'

        return render_template('results.html',result=result)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        try:
            operation=request.json['operation']
            num1=int(request.json['num1'])
            num2 = int(request.json['num2'])
            if(operation=='add'):
                r=num1+num2
                result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
            if (operation == 'subtract'):
                r = num1 - num2
                result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'multiply'):
                r = num1 * num2
                result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'divide'):
                r = num1 / num2
                result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            return jsonify(result)

        except Exception as e:
            return jsonify("Value Error Occurs. Please check the input and try again!!")


if __name__ == '__main__':
    app.run(debug=True)
