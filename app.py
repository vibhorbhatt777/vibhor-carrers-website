from flask import Flask 

app = Flask(__name__)

@app.route("/")#part of the url after domain name
def hello():
     return "<p> Hello world </p>"
  
