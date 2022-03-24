"""
Web-App based on flask library
"""
from flask import *
from flask import request
import os
from simpletransformers.classification import ClassificationModel, ClassificationArgs
from transformers import RobertaTokenizer

# predict function sets the classify the SMS as ham or spam
from predict import prediction

application = app = Flask(__name__)


@app.route('/')
def upload():
    return render_template("index.html")


@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print("started flask")
        sms = request.form['sms']
        print(sms)
        print("performing prediction")
        label = prediction(sms)
        return render_template("index.html", label=label)
    else:  # if no file was chosen
        print("no file chosen")
        return render_template("index.html", error="You have to insert a text!")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
