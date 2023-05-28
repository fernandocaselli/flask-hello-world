from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    resp = make_response("Hello, World 2!")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/about')
def about():
    resp = make_response("About 2")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
