from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'

@app.route('/')
def show_home_page():
    """ Shows home page """
    return render_template('index.html')