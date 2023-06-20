# Importing necessary libraries
from flask import Flask, render_template, request
from joblib import load
import pandas as pd

clf = load('model_files/bank_deposit_classification.joblib')
ct = load('model_files/column_transformer.joblib')
label_encoder = load('model_files/label_encoder.joblib')

app = Flask(__name__)


def processData(data, colNames):
    new_data = pd.DataFrame([data], columns=colNames)
    X_new_encoded = pd.DataFrame(ct.transform(new_data))
    y_new_pred = clf.predict(X_new_encoded)
    prediction_label = label_encoder.inverse_transform(y_new_pred)

    return prediction_label


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    listOfColNames = ['age', 'job', 'marital', 'education', 'default', 'balance', 'housing',
                      'loan', 'contact', 'day', 'month', 'campaign', 'pdays', 'previous',
                      'poutcome']
    num_cols = ['age', 'balance', 'day', 'campaign', 'pdays', 'previous']
    if request.method == 'POST':
        data = [int(request.form[i]) if i in num_cols else request.form[i] for i in listOfColNames]
        cls_result = processData(data, listOfColNames)  # Add return statement here

        # Add a default response in case the method is not POST
        return render_template('index.html', result=cls_result[0])


if __name__ == '__main__':
    app.run(debug=True)