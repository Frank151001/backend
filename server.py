from flask import Flask, request,abort
import json
from about import me
from config import db
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
 
# WEB SERVER #
@app.get("/")
def home():
    return "Hello world"

@app.get("/test")
def test():
    return "Its a test page"

# API SERVER #
@app.get("/api/version")
def version():
    return json.dumps("1.0")

@app.get("/api/about")
def about():
    return json.dumps(me)

@app.get("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    results =  []
    for prod in cursor:
        results.append(fix_id(prod))
    return json.dumps(results)

def fix_id(record):
    record["_id"] = str(record["_id"])
    return record

@app.post("/api/catalog")
def save_product():
    product = request.get_json()
    db.products.insert_one(product)
    print("-----------------------")
    print(product)
    return json.dumps(fix_id(product))

@app.get("/api/products/count")
def product_count():
    count= db.products.count_documents({})
    return json.dumps(count)

@app.get("/api/products/total")
def product_total():
    cursor = db.products.find({})
    total = 0
    for product in cursor:
        price = product["price"]
        total = total + price
    return json.dumps(total)

@app.get('/api/categories')
def categories():
    cursor = db.products.find({})
    cats = []
    for product in cursor:
        category = product["category"]
        if category not in cats:
            cats.append(category)
    return json.dumps(cats)    

@app.get("/api/developer/name")
def developer_name():
    name=me["name"]
    last=me["last_name"]
    email=me["email"]
    response =f"{name} {last} -- {email}"
    return json.dumps(response)


@app.get("/api/catalog/<category>")
def product_by_category(category):
    cursor = db.products.find({"category": category})
    results = []
    for prod in cursor:
        results.append(fix_id(prod))
    return json.dumps(results)

@app.get("/api/products/lower/<price>")
def products_lower_price(price):
    fixed_price = float(price)
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        if prod["price"] < fixed_price:
            results.append(fix_id(prod))
    return json.dumps(results)

@app.get("/api/products/greater/<price>")
def products_greater_price(price):
    fixed_price = float(price)
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        if prod["price"] >= fixed_price:
            results.append(fix_id(prod))
    return json.dumps(results)

@app.get("/api/products/search/<term>")
def search_products(term):
    cursor = db.products.find({"title": {"$regex": term, "$options": "i"}})
    results = []
    for prod in cursor:
        results.append(fix_id(prod))
    return json.dumps(results)

#Coupon Codes#
@app.post("/api/coupons")
def save_coupon():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)
    return json.dumps(fix_id(coupon))

@app.get("/api/coupons")
def get_coupons():
    cursor = db.coupons.find({})
    results = []
    for coupon in cursor:
        results.append(fix_id(coupon))
    return json.dumps(results)

@app.get("/api/coupons/<code>")
def get_coupon_by_code(code):
    coupon = db.coupons.find_one({"code": code})
    if coupon == None:
        return abort(404,"Invalid coupon code")
    return json.dumps(fix_id(coupon))

#start the server
app.run(debug=True)