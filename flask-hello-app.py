from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
        return 'Hello World'

#--------------------------------------
#export FLASK_APP=flask-hello-app.py
#python -m flask run
#--------------------------------------
