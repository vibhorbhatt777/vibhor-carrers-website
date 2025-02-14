from flask import Flask 

app = Flask(__name__)

@app.route("/")#part of the url after domain name
def hello():
     return "<p> Hello Vibhor </p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0' , debug=True)
  

