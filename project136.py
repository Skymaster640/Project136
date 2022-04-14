import pandas as pd

from flask import Flask,jsonify,request
from stardata import stardata
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data":stardata,
        "message":"Success"

    }),200

@app.route("/star")
def star():
    name = request.args.get('Star_name')
    star_data = next(item for item in stardata if item["Star_name"]==name)
    return jsonify({
        "data":star_data,
        "message":"Success"
    }),200

if __name__ == "__main__":
    app.run()