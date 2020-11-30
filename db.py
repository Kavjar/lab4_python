from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from wsgiref.simple_server import make_server

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
    user='root', password='j27333', server='localhost', database='test')
db = SQLAlchemy(app)

engine = db.engine
Base = db.Model
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/v1/hello-world-28!')
def number_display( ):
    return 'Hello, World - 28' , 200

with make_server('', 5000, app) as server:
 print("pracue yra")

 server.serve_forever()