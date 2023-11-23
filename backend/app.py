from flask import Flask, jsonify, request
from dotenv import load_dotenv
from pymongo import MongoClient
from objects import Product, SalesPerson, Customer, Sales, Discount
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
'''


app = Flask(__name__)

#implement api endpoints for each route

#products
@app.route('/products', methods=['GET', 'POST'])
def manageProducts():
    if request.method == "GET":
        products = db.products.find()
        return jsonify([product for product in products])
    elif request.method == "POST":
        productData = request.json
        product = Product(**productData)
        db.products.insert_one(product.to_json())
        return jsonify(product.to_json()), 201

#Salesperson
@app.route('/salesperson', methods=['GET', 'POST'])
def manageSalesPeople():
    if request.method == "GET":
        salesPerson = db.salesPerson.find()
        return jsonify([person for person in salesPerson])
    elif request.method == "POST":
        peopleData = request.json
        person = SalesPerson(**peopleData)
        db.salesPerson.insert_one(salesPerson.to_json())
        return jsonify(person.to_json()), 201
#Customer
@app.route('/customer', methods=['GET', 'POST'])
def manageCustomers():
    if request.method == "GET":
        customers = db.customers.find()
        return jsonify([customer for customer in customers])
    elif request.method == "POST":
        customerData = request.json
        customer = Customer(**customerData)
        db.customers.insert_one(customer.to_json())
        return jsonify(customer.to_json()), 201
#Sales
@app.route('/sales', methods=['GET', 'POST'])
def manageSales():
    if request.method == "GET":
        sales = db.sales.find()
        return jsonify([sale for sale in sales])

    elif request.method == "POST":
        saleData = request.json
        sale = Product(**saleData)
        db.sales.insert_one(sale.to_json())
        return jsonify(sale.to_json()), 201
#Discount
@app.route('/discount', methods=['GET', 'POST'])
def manageDiscounts():
    if request.method == "GET":
        discounts = db.discounts.find()
        return jsonify([discount for discount in discounts])

    elif request.method == "POST":
        discountData = request.json
        discount = Product(**discountData)
        db.discounts.insert_one(discount.to_json())
        return jsonify(discount.to_json()), 201


def home():
    return "Home"

if __name__ == '__main__':
    app.run(debug=True)