# This isn't actually part of the Flakr app, but rather a dummy page
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, World!'
