import pymongo
from flask import Flask,jsonify,render_template,request
from flask_pymongo import PyMongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://admin:GFHsax21310@10.100.2.83:27017") 
db = client["Ass1"] 


@app.route("/") 
def index(): 
    emp_list = db.Car.find()
    return render_template('index.html', emp_list = emp_list)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port = 80 , debug=True)