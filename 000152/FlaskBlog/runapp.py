from flask import Flask, redirect, url_for, render_template, request
from sklearn.externals import joblib
import numpy as np
app = Flask(__name__)
from FlaskBlog.flaskblog import app


@app.route("/about")
def about():
	return render_template("about.html")

def ValuePredictor(to_predict):
    loaded_model = joblib.load('house_price_res.pickle')
    result = loaded_model.predict(np.array(to_predict).reshape(1, -1))
    return result

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        result = list(result.values())
        result = list(map(int, result))
        result = ValuePredictor(result)
        # return render_template("result.html", prediction=prediction)
        # return result
        return render_template("result.html",prediction=result)

if __name__=="__main__":
	app.run(debug=True,port='9090')