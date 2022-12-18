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

@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml')

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

# @app.route('/search', methods=['POST'])
# def search():
#     name = request.form.get('LINE')
#     print(df[df["帳號"]==name].to_dict())
#     if name:
#        print('Request for hello page received with name=%s' % name)
#        return jsonify(jsonStr)
#     else:
#         print('Request for hello page received with no name or blank name -- redirecting')
#         return redirect(url_for('index'))

if __name__ == '__main__':
   app.run()