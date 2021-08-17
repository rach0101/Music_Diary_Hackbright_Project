"""Server for Music Diary App"""

from flask import Flask, jsonify, render_template
from model import connect_to_db
import crud


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# @app.route("/login", method=["POST"])

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
