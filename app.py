from flask import Flask, render_template, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    date = datetime.now()
    formatted_date = date.strftime("%d-%m-%Y")
    return render_template('index.html', date=formatted_date)

@app.route('/profile')
def profile():
    return redirect('/')

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
