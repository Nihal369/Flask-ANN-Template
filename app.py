from flask import Flask
from flask import request
from flask import jsonify
import Interface as pd
app = Flask(__name__)
@app.route("/predict",methods=['POST'])


def predict():
    result = pd.predict(request.form['your_parameter_1'],request.form['your_parameter_2'])
    res={}
    #KEY NAME: VALUE
    res['value']= str(result[0][0])
    return jsonify(res)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
