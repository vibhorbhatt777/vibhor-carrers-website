from flask import Flask , render_template , jsonify

app = Flask(__name__)

JOBS = [
   {
         'id': 1,
         'title':'Data Analyst',
         'location':'Bengalaru, India',
          'salary': 'Rs. 10,00,000'
     },

     {
         'id': 2,
         'title':'Data Scientisit',
         'location':'Delhi, India',
          'salary': 'Rs. 15,00,000'
     },
     {
         'id': 3,
         'title':'Front-end Engineer',
         'location':'Remote',
          'salary': 'Rs. 12,00,000'
     },
     {
         'id': 4,
         'title':'Back-end-Engineer',
         'location':'Pune, India',
          'salary': 'Rs. 18,00,000'
     },
     
     
     
     
]

@app.route("/")
def hello_vibhor():
       return render_template(
            'home.html',
            jobs = JOBS,
            company_name = 'Vibhor'
       )
@app.route("/jobs")
def list_jobs():
       return jsonify(JOBS)
     
@app.route("/")#part of the url after domain name
def hello():
     return render_template("home.html", jobs=JOBS,company_name="Vibhor")


     
     

if __name__ == "__main__":
    app.run(host='0.0.0.0' , debug=True)
  

