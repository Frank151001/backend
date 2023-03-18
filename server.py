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

@app.get("/api/developer/name")
def developer_name():
    name=me["name"]
    last=me["last_name"]
    email=me["email"]
    response =f"{name} {last} -- {email}"
    return json.dumps(response)



#start the server
app.run(debug=True)