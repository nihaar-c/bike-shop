#store objects and base structure of transactions


#general skeleton -- repeatable for most object types

#product
class Product:
    def __init__(self, name, manufacturer, style, purchasePrice, salePrice, currentAmt, comission):
        self.name = name
        self.manufacturer = manufacturer
        self.style = style
        self.purchasePrice = purchasePrice
        self.salePrice = salePrice
        self.currentAmt = currentAmt
        self.comission = comission
    
    def to_json(self):
        return {
            "name": self.name,
            "manufacturer": self.manufacturer,
            "style": self.style,
            "purchasePrice": self.purchasePrice,
            "salePrice": self.salePrice,
            "currentAmt": self.currentAmt,
            "comission": self.comission
        }

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
                