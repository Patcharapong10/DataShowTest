import pymongo
import http.client
import bson
from flask import Flask,jsonify,render_template,request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

conn = http.client.HTTPSConnection("car-stockpile.p.rapidapi.com")
app = Flask(__name__)
client = pymongo.MongoClient("mongodb://admin:VIDgnh48123@node12713-project.app.ruk-com.cloud:11012") 
db = client["project"] 


@app.route("/") 
def index(): 
    emp_list = db.car.find().limit(3)
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
    shop_list = db.car.find()
    return render_template('shop.html', shop_list = shop_list)

@app.route("/product/<id>")
def clickpro(id):
    pro = db.msg.find_one({'_id': ObjectId(id)})
    return render_template('product.html', pro = pro)


#////////////////////////////////////////////////////////
#ทำการ insert ข้อมูลตารางเข้าไปใหม่
@app.route('/insertuser', methods=['POST'])
def insertuser():
  char = db.customer
  email = request.form['email'] 
  firstname = request.form['firstname']
  lastname = request.form['lastname']
  password = request.form['password']
  coin = request.form['coin']
  address = request.form['address']
  char.insert_one({ 'email' : email, 'firstname' : firstname, 'lastname': lastname, 'password' : password, 'coin':coin , 'address': address})
  return render_template('AdminEdit.html')

@app.route('/insertcar', methods=['POST'])
def insertcar():
  char = db.car
  _name = request.form['_name'] 
  _model = request.form['_model']
  _price = request.form['_price']

  char.insert_one({ '_name' : _name, '_model' : _model, '_price': _price})
  return render_template('AdminCar.html')

#ทำการ edit ข้อมูลตารางโดยการอิง name or _name
@app.route('/Car/<name>', methods=['PUT'])
def update_character(name):
    char = db.Car
    x = char.find_one({'_name' : name}) #เอาค่าที่ใส่มาใน name เพื่อเช็คว่าตรงกับตารางไหน
    if x: #ในตัวแปร x มี name ที่เรากรอกลงไปใน /Car/<name>
        myquery = {'_name' : x['_name'], #เรียกข้อมูลมาใส่ใน myquery
                        '_model' : x['_model'],
                        '_price' : x['_price']}

    name = request.json['_name'] #ทำการสร้างตัวแปรใหม่เพื่อรับค่าจาก _name
    model = request.json['_model']
    price = request.json['_price']
    
    newvalues = {"$set" : {'_name' : name,  #ทำการแก้ไขไฟล์แล้วใส่ไปในตัวแปรที่ส้รางรวมกันเป็นอาเร
                        '_model': model,
                        '_price': price,}}
    char_id = char.update_one(myquery, newvalues) #ส่งไปอัพเดท
    output = {'_name' : name,  #นำค่าที่อัพเดทมาทั้งหมดลงตัวแปร output
                        '_model': model,
                        '_price': price,}
    return jsonify(output) #หลังจากทำเงื่อนไขเสร็จส่งค่ากลับไปที่ output

#ทำการ Deleted ข้อมูลตารางโดยการอิง name or _name
@app.route('/Car/<name>', methods=['DELETE'])
def Car_delete(name):
    char = db.Car
    x = char.find_one({'_name' : name}) #ในตัวแปร x มี name ที่เรากรอกลงไปใน /Car/<name>

    char_id = char.delete_one(x) #นำ x มาทำฟังชัั่น delete_one 

    output = "Deleted complete" # หลังจากลบเสร็จแสดงข้อความ

    return jsonify(output) #หลังจากทำเงื่อนไขเสร็จส่งค่ากลับไปที่ output

#////////////////////////////////////////////////////////

if __name__ == "__main__":
    app.run(host='127.0.0.1',port = 80)