from flask import  Flask,render_template,url_for,request
import joblib
import re
import string
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
Model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template("index.html")

def wordpre(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) # remove special chars
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

@app.route('/input',methods=['POST'])
def pre():
    if request.method == 'POST':
        txt = request.form['txt']
        txt = wordpre(txt)
        txt = pd.Series(txt)
        # pd.Series(txt) wenne me dee
        # d = {'a': 1, 'b': 2, 'c': 3}
        # ser = pd.Series(data=d, index=['a', 'b', 'c'])
        # ser
        # a   1
        # b   2
        # c   3
        result = Model.predict(txt)
        return render_template("index.html", result = result)
    return '' 
if __name__ == "__main__":
    app.run()