from flask import Flask, render_template, redirect, request, jsonify
from piencrypt import pie
import random
from data import*

app = Flask(__name__)

Texts = ['Hi', 'Solo', 'Sid', 'Test', 'Lily', 'Python', 'Throttlerz', 'Password', 'Good Morning', 'Good Evening']   

def infile_quality_test():
    for i in range(10):
        data = []
        for i in range(5000):
            r = random.choice(Texts)
            data.append(r)
  
        input = ", ".join(data)
        try:
            r = pie.PiEncrypt('pic.png')
            r.get_data()
            r.hide_data(input)
            output = r.read_data()
            r.revert()
            # print(output, end=r" %FINISHED% ")
        except Exception as e:
            raise ValueError(e)

def infile_quantity_test():
    for i in range(1000):
        data = []
        for i in range(5):
            r = random.choice(Texts)
            data.append(r)
  
        input = ", ".join(data)
        try:
            r = pie.PiEncrypt('pic.png')
            r.get_data()
            r.hide_data(input)
            output = r.read_data()
            r.revert()
            # print(output, end=r" %FINISHED% ")
        except Exception as e:
            raise ValueError(e)
  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test/<name>')
def test(name):
    if name == "sid86":
        try:
            infile_quality_test()
            infile_quantity_test()        
            return jsonify(PiEncrypt=hash) # Returns HTTP Response for testing
        except:
            return "Test Failed"
    else:
        return "Test not allowed"

if __name__ == "__main__":
    app.run(debug=True, port=4000)