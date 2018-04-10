import numpy as np
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"

db = SQLAlchemy(app)

class BellyButton(db.Model):
    __tablename__ = 'belly button'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<Belly Button %r>' % (self.nickname)

@app.route("/names", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        sample = request.form["sample"]
        gender = request.form["gender"]

        BellyButton = sample(nickname=nickname, gender=gender)
        db.session.add(BellyButton)
        db.session.commit()

    




@app.route("/otu")
def list_BellyButton():
    results = db.session.query(BellyButton.nickname, BellyButton.age).all()

    pets = []
    for result in results:
        pets.append({
            "sample": result[0],
            "gender": result[1]
        })
    return jsonify(BellyButton)


@app.route("/")
def home():
    return "This is Homework!"

if __name__ == "__main__":
    app.run()
