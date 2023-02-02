from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_xxx():
    return 'Hello, XXX!'
