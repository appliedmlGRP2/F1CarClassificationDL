import os
import random

from flask import *
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from sqlalchemy import create_engine, types
import sqlite3
import json
import io
import glob
from PIL import Image
from torchvision import models
import torchvision.transforms as transforms
import torch
from werkzeug.utils import secure_filename

classes = ['Alpha Tauri F1 Team','Scuderia Ferrari F1 Team','McLaren F1 Team','Mercedes AMG Petronas F1 Team','Racing Point','Oracle Red Bull Racing Honda','Renault F1 Team',
           'Williams F1 Team']

app = Flask(__name__)

UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"


def get_prediction(filename):
    print("Inside get prediction")
    model = torch.load("mobilenet_v2-full.bin", map_location=torch.device("cpu"))
    data_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    image = Image.open(UPLOAD_FOLDER + "/" + filename)
    img = data_transforms(image).unsqueeze(0)
    output = model(img)
    _, predicted = torch.max(output, 1)
    print(_)
    print(predicted)
    return classes[predicted]
    # print(output)


@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("index.html",messages=False)
    if request.method=="POST":
        print("got post")
        print(request.files)
        if 'file' not in request.files:
            print("File not there")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print("No file selected")
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            print("File received")
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # get_prediction(filename)
            label = get_prediction(filename)
            flash(label)
            # flash(acc)
            # flash(filename)
            # return redirect('/')
            return render_template("index.html",messages=True,img_path=os.path.join(app.config['UPLOAD_FOLDER'],filename))





if __name__=='__main__':
    app.run(debug=True)
