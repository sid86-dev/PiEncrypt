from flask import Flask, render_template, request, jsonify
from piencrypt import pie
import random

hash = '03c1d04aeffd72151933b2295df5b484547e00ead9d001126aef03e6179a9332'
app = Flask(__name__)

Texts = ['Hi', 'Solo', 'Sid', 'Test', 'Lily', 'Python', 'Throttlerz', 'Password', 'Good Morning', 'Good Evening']   


p = pie.PiEncrypt('pic.png')

def infile_quality_test():
    test = "pass"
    for i in range(5):
        data = []
        for m in range(500):
            r = random.choice(Texts)
            data.append(r)
        input = ", ".join(data)
        try:
            p.get_data()
            p.hide_data(input)
            output = p.read_data()
            if output != input:
                test = "fail"
            p.revert()
            # print(output, end=r" %FINISHED% ")
        except Exception as e:
            test = "fail"
            raise ValueError(e)
    return test 

def infile_quantity_test():
    test = "pass"
    for i in range(500):
        data = []
        for m in range(5):
            r = random.choice(Texts)
            data.append(r)
  
        input = ", ".join(data)
        try:
            p.get_data()
            p.hide_data(input)
            output = p.read_data()
            if output != input:
                test = "fail"
            p.revert()
            # print(output, end=r" %FINISHED% ")
        except Exception as e:
            test = "fail"
            raise ValueError(e)
    return test
  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test/<string:name>')
def test(name):
    if name == "sid86":
        try:
            result1 = infile_quality_test()
            result2 = infile_quantity_test()
            # print(result1)
            # print(result2)
            if result1 == "pass" and result2 == "pass":
                return jsonify(PiEncrypt=hash) # Returns HTTP Response for testing
            else:
                return "Test Failed"
        except:
            return "Test Failed"
    else:
        return "Test not allowed"

if __name__ == "__main__":
    app.run(debug=True)