from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ianno2@127.0.0.1:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Mode):
        __tablename__='persons'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(), nullable=False)

        def __repr__(self):
                return f'<Person ID: {self.id}, name:{self.name}'
@app.route('/')
def index():
        person = Person.query.first()
        return 'Hello ' + person.name