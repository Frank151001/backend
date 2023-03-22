from flask import Flask
import json
from about import me
from data import mock_data
app= Flask("__server__") #create a instance of flask class
 

@app.get("/")
def home():
    return "Hello world"

@app.get("/test")
def test():
    return "Its a test page"


@app.get("/api/version")
def version():
    return json.dumps("1.0")

@app.get("/api/about")
def about():
    return json.dumps(me)


@app.get("/api/catalog")
def catalog():
    return json.dumps(mock_data)

@app.get("/api/products/count")
def product_count():
    count=len(mock_data)
    return json.dumps(count)

@app.get("/api/products/total")
def product_total():
    total=0
    for product in mock_data:
        price=product ["price"]
        total = total+ price
    return json.dumps(total)

@app.get('/api/categories')
def categories():
    cats = []
    for product in mock_data:
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
    P_list=[]
    for prod in mock_data:
        if prod["category"].lower()==category.lower():
            P_list.append(prod)
    return json.dumps(P_list)

#start the server
app.run(debug=True)