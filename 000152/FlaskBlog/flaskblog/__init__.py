from flask import Flask, redirect, url_for, render_template, request
from sklearn.externals import joblib
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

def ValuePredictor(to_predict):
    loaded_model = joblib.load('C:\\Users\\Pinky\\Desktop\\Project\\house_price_res.pickle')
    result = loaded_model.predict(np.array(to_predict).reshape(1, -1))
    return result

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        result = list(result.values())
        result = list(map(float, result))
        result = ValuePredictor(result)
        # # return render_template("result.html", prediction=prediction)
        # return result
        return render_template("result.html",prediction=result)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from FlaskBlog.flaskblog import routes