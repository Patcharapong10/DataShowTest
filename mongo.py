import pymongo
from flask import Flask,jsonify,render_template,request
from flask_pymongo import PyMongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://admin:VIDgnh48123@node12713-project.app.ruk-com.cloud:11012") 
db = client["Ass1"] 


@app.route("/") 
def index(): 
    emp_list = db.Car.find()
    return render_template('index.html', emp_list = emp_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 80)