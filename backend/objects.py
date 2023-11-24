#store objects and base structure of transactions


#general skeleton -- repeatable for most object types

#product
class Product:
    def __init__(self, name, manufacturer, style, purchasePrice, salePrice, currentAmt, commission):
        self.name = name
        self.manufacturer = manufacturer
        self.style = style
        self.purchasePrice = purchasePrice
        self.salePrice = salePrice
        self.currentAmt = currentAmt
        self.commission = commission
    
    def to_json(self):
        return {
            "Name": self.name,
            "Manufacturer": self.manufacturer,
            "Style": self.style,
            "Purchase Price": self.purchasePrice,
            "Sale Price": self.salePrice,
            "Current Amount": self.currentAmt,
            "Commission": self.commission
        }
'''
api request test
{
	"name": "iPhone",
	"manufacturer": "Apple",
  "style": "Red",
  "purchasePrice": 200,
  "salePrice": 500,
  "currentAmt": 100,
  "commission": 0.2
}
'''

#salesperson
class SalesPerson:
    def __init__(self, firstName, lastName, address, phone, startDate, endDate, manager):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.phone = phone
        self.startDate = startDate
        self.endDate = endDate
        self.manager = manager
    
    def to_json(self):
        return {
            "First Name": self.firstName,
            "Last Name": self.lastName,
            "Address": self.address,
            "Phone Number": self.phone,
            "Start Date": self.startDate,
            "End Date": self.endDate,
            "Manager": self.manager
        }

#customer
class Customer:
    def __init__(self, firstName, lastName, address, phone, startDate):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.phone = phone
        self.startDate = startDate
    
    def to_json(self):
        return {
            "First Name": self.firstName,
            "Last Name": self.lastName,
            "Address": self.address,
            "Phone Number": self.phone,
            "Start Date": self.startDate
        }
#sales
class Sales:
    def __init__(self, product, salesperson, customer, date):
        self.product = product
        self.salesperson = salesperson
        self.customer = customer
        self.date = date
    
    def to_json(self):
        return {
            "Product": self.product,
            "Sales Person": self.salesperson,
            "Customer": self.customer,
            "Date": self.date
        }
'''
{
	"product": "iPhone",
	"salesperson": "Mike",
	"customer": "Nihaar",
	"date": "11/23/23"
}'''
#discount
class Discount:
    def __init__(self, product, startDate, endDate, amt):
        self.product = product
        self.startDate = startDate
        self.endDate = endDate
        self.amt = amt
    
    def to_json(self):
        return {
            "Product": self.product,
            "Start Date": self.startDate,
            "End Date": self.endDate,
            "Discount Amount": self.amt
        }
                