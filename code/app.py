from flask import Flask
from flask_restful import Api
from resources.plate import Plate, PlateList
from db import db
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

api.add_resource(Plate, '/plate')
api.add_resource(PlateList, '/plate')

if __name__ == '__main__':
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
