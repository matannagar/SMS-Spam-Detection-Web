"""
Web-App based on flask library
"""
from flask import *
from flask import request
import os
from simpletransformers.classification import ClassificationModel, ClassificationArgs
from transformers import RobertaTokenizer
# import torch

# predict function sets the classify the SMS as ham or spam
from predict import performPrediction

application = app = Flask(__name__)

model_args = ClassificationArgs(num_train_epochs=1,use_multiprocessing=False
                                ,use_multiprocessing_for_evaluation=False, process_count= 1)
model = ClassificationModel(
            "roberta", "C:/Users/matan/My PC (DESKTOP-RLTMVS3)/Desktop/simpletransformers_project/outputs",
            args=model_args, use_cuda=False)
tokenizer = RobertaTokenizer.from_pretrained("C:/Users/matan/My PC (DESKTOP-RLTMVS3)/Desktop/simpletransformers_project/outputs")

from transformers import RobertaTokenizer
def prediction_test(text):
    """Simple function for Flask with no bells and whistles"""

    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.model(**inputs)

    return outputs

# homepage
@app.route('/')
def upload():
    return render_template("index.html")


@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print("started flask")
        max_words = request.form['max-words']
        print(max_words)
        #
        # #
        # # # Create a ClassificationModel
        # cuda_available = torch.cuda.is_available()
        # cuda_available = False
        #
        # # Create a ClassificationModel
        # # this loads the models from the output directory
        # print("starting to load model")

        print("performing prediction")

        # try:
        #     predictions, raw_outputs = model.predict([max_words])
        # except:
        #     print("something went wrong with prediction")
        # print("returning prediction")
        # summary = performPrediction(max_words)
        # summary = predictions[0]
        test = prediction_test(max_words)
        print(test[0][0][0].item())
        print(test[0][0][1].item())

        if test[0][0][0].item() > test[0][0][1].item():
            summary = "Non-Spam"
        else:
            summary = "Spam"

        # summary = "oops"
        print(summary)
        return render_template("index.html", summary=summary)
        # glob_var = summary
        # session['my_var'] = summary
    else:  # if no file was chosen
        print("no file chosen")
        return render_template("index.html", error="You have to insert a text!")
    # else:
    #     return render_template("index.html", summary=glob_var)


# need to be erased
if __name__ == '__main__':
    app.run(host="0.0.0.0")
