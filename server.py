from flask import Flask
import json
from about import me

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


#start the server
app.run(debug=True)