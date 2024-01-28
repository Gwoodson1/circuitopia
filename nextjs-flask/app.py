from flask import Flask, render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
    return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return render_template('gameon.html', score = 0)
   
    return render_template('index.html')

@app.route('/gameon', methods=['POST', 'GET'])
def gameon():
    score += 1
    return render_template('gameon.html', score = score)

@app.route('/gameover', methods=['POST', 'GET'])
def gameover():
    return render_template('gameover.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True)