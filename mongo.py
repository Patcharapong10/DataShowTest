import pymongo
import http.client
from flask import Flask,jsonify,render_template,request
from flask_pymongo import PyMongo

conn = http.client.HTTPSConnection("car-stockpile.p.rapidapi.com")
app = Flask(__name__)
client = pymongo.MongoClient("mongodb://admin:VIDgnh48123@node12713-project.app.ruk-com.cloud:11012") 
db = client["Ass1"] 



@app.route("/") 
def index(): 
    emp_list = db.Car.find().limit(3)
    return render_template('index.html', emp_list = emp_list)

#///////////////////////////////////////////////////////////////////////////

@app.route("/AdminEdit")
def AdminEdit():
    return render_template("AdminEdit.html")


@app.route("/About")
def About():
    return render_template("About.html")
    
@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/Login")
def Login():
    return render_template("Login.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/Register")
def Register():
    return render_template("Register.html")

@app.route("/shop")
def shop():
    shop_list = db.Car.find()
    return render_template('shop.html', shop_list = shop_list)


if __name__ == "__main__":
    app.run(host='127.0.0.1',port = 80)