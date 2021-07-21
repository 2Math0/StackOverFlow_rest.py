from flask import Flask, request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Unsolved(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return 'Hello'

@app.route('/questions')
def get_questions():
    ques = Unsolved.query.all()
    dic_query = []

    for q in ques:
        dic_query.append({'name' : q.name, 'description' : q.description})

    return {'question': dic_query}

@app.route('/questions/<id>')
def get_questions(id):
    ques = Unsolved.query.get_or_404(id)
    return jsonify({'name': ques.name, 'description' : ques.description})

@app.route('/questions', methods=['POST'])
def add_question():
    ques = Unsolved(name=request.json['name'], description=request.json['description'])
    db.session.add(ques)
    db.session.commit()
    return {'id' : ques.id}

@app.route('/questions/<id>', methods=['DELETE'])
def delete_question(id):
    ques = Unsolved.query.get(id)
    if ques is None:
        return jsonify({'error' : 'Not Found 404'})
    db.session.delete(ques)
    db.session.commit()
    return {'message' : 'smashed'}