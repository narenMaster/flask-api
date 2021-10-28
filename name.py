from flask import Flask,jsonify,request
from data import data

app = Flask(__name__)
@app.route("/")

def router() :
    return "ABSOLUTELY WELCOME !"

@app.route("/anyname")

def secondrouter() :
    return jsonify({
        "data" : data ,
        "message" : "SUCCESS"
    }),200

@app.route('/sinname')   

def thirdrouter() :
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name )
    return jsonify({
        "data" : planet_data ,
        "message" : "404 PLANET FOUND"
    }),200
    
    

if __name__ == "__main__" :
    app.run()
