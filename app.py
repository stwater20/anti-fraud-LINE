from datetime import datetime
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory , jsonify,make_response
import requests
import urllib.request
import pandas as pd
import json
from flask_wtf.csrf import CSRFProtect

def download_data():
    try:
        res = urllib.request.urlretrieve("https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=7F6BE616-8CE6-449E-8620-5F627C22AA0D", "dataset.csv")
        return res
    except Exception as e:
        print(e)
        return False

def get_data():
    data = pd.read_csv('dataset.csv')
    return data
    
df = get_data()
dataset = df.values.tolist()
jsonStr = json.dumps(dataset)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
 
csrf = CSRFProtect()
csrf.init_app(app)


@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html',dataset=dataset)

@app.route('/updatedsfdsfl;ewtjr;wefewfdsf;mewrfkew;fdkfgop[ewrtjopdfdsf;dsf,sefdsfsefefsdefdsf')
def update():
    try:
        download_data()
        return render_template('success.html')
    except:
        return render_template('error.html',503)

@app.route('/data',methods=["POST"])
def data():
    return jsonify(dataset)


if __name__ == '__main__':
   app.run()