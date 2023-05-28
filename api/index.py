from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World 2!'

@app.route('/about')
def about():
    return 'About 2'

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
