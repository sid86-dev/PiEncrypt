from flask import Flask, render_template, redirect, request, secure_filename
from main import get_binary,process_pic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['GET', 'POST'])
def process():
    if request.method == "POST":
        get_binary()       
    return render_template('download.html')

if __name__ == "__main__":
    app.run(debug=True, port=4000)