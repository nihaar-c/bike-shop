from flask import Flask, jsonify, request
from dotenv import load_dotenv
from pymongo import MongoClient
from objects import Product, SalesPerson, Customer, Sales, Discount
from bson import ObjectId
import os

#access Mongo connection string from .env
load_dotenv()
connectionString = os.getenv("mongoConnectionString")

#create mongo client and access database
client = MongoClient(connectionString)
db = client['EntityData']
'''
#testing connection
collection = db['Sample Test V1']
test_doc = {"name": "Test", "msg": "Testing testing"}
result = collection.insert_one(test_doc)
print (f"Test doc inteseted with _id: {result.inserted_id}")
retrieved_doc = collection.find_one({"name": "Test"})
print(f"Retrieved doc: {retrieved_doc}")

test_doc = {
	"product": "iPhone",
	"salesperson": "Mike",
	"customer": "Nihaar",
	"date": "11/22/23"
}
result = db['Sales'].insert_one(test_doc)
print (f"Test doc inteseted with _id: {result.inserted_id}")
'''

app = Flask(__name__)

#implement api endpoints for each route


#convert objectid to string
def bsonToJson(data):
    for doc in data:
        doc["_id"] = str(doc["_id"])
    return data

#products
@app.route('/products', methods=['GET', 'POST'])
def manageProducts():
    if request.method == "GET":
        productsCursor = db['Products'].find()
        products = list(productsCursor)
        return jsonify(bsonToJson(products))
    elif request.method == "POST":
        productData = request.json
        print(f"{productData}")
        product = Product(**productData)
        db['Products'].insert_one(product.to_json())
        return jsonify(product.to_json()), 201

#Salesperson
@app.route('/salesperson', methods=['GET', 'POST'])
def manageSalesPeople():
    if request.method == "GET":
        salesPersonCursor = db['Salesperson'].find()
        salesPerson = list(salesPersonCursor)
        return jsonify(bsonToJson(salesPerson))
    elif request.method == "POST":
        peopleData = request.json
        person = SalesPerson(**peopleData)
        db.salesPerson.insert_one(salesPerson.to_json())
        return jsonify(person.to_json()), 201
#Customer
@app.route('/customer', methods=['GET', 'POST'])
def manageCustomers():
    if request.method == "GET":
        customersCursor = db['Customers'].find()
        customers = list(customersCursor)
        return jsonify(bsonToJson(customers))
    elif request.method == "POST":
        customerData = request.json
        customer = Customer(**customerData)
        db.customers.insert_one(customer.to_json())
        return jsonify(customer.to_json()), 201
#Sales
@app.route('/sales', methods=['GET', 'POST'])
def manageSales():
    if request.method == "GET":
        salesCursor = db['Sales'].find()
        sales = list(salesCursor)
        return jsonify(bsonToJson(sales))
    elif request.method == "POST":
        saleData = request.json
        sale = Sales(**saleData)
        db.sales.insert_one(sale.to_json())
        return jsonify(sale.to_json()), 201
#Discount
@app.route('/discount', methods=['GET', 'POST'])
def manageDiscounts():
    if request.method == "GET":
        discountsCursor = db['Discounts'].find()
        discounts = list(discountsCursor)
        return jsonify(bsonToJson(discounts))

    elif request.method == "POST":
        discountData = request.json
        discount = Discount(**discountData)
        db.discounts.insert_one(discount.to_json())
        return jsonify(discount.to_json()), 201

#business logic -- commissions & bonuses

#comission by sale
def calculateCommission(product):
    product = db['Products'].find({"Name": product})
    product = list(product)
    print (product)
    return (product[0]["Commission"] * product[0]["Sale Price"] if product else 0)

@app.route('/commissions', methods=['POST'])
def getCommission():
    sale = request.json
    sale = Sales(**sale)
    commission = calculateCommission(sale.product)
    return jsonify({"Commission": commission}), 200

#bonus
#salesperson to find bonus of
def calculateBonus(sales, person):
    totalCommission = 0
    for i in sales:
        if person == i['salesperson']:
            totalCommission += calculateCommission(i)
    
    return int(0.5 * totalCommission)
#not working -- need to investigate more to fix
@app.route('/bonus/<personID>', methods=['GET'])
def getBonus(personID):
    #sales = db.sales.find({"Sales Person": personID})
    #sales = list(sales)
    #del sales[0]['_id']
    #print(sales[0])
    sales = db['Sales'].find()
    sales = list(sales)
    print(sales)

    calculateBonus(sales, personID)
    #return jsonify({"bonus": bonus}), 200        


def home():
    return "Home"

if __name__ == '__main__':
    app.run(debug=True)