from flask_restful import Resource, reqparse
from models.plate import PlateModel, PlateValidation
from resources.ServiceResponse import missing_request, invalid_plate, valid_plate
from flask import request, jsonify
from datetime import datetime


class Plate(Resource):
    parser = reqparse.RequestParser()

    def post(self):
        #import pdb
        #pdb.set_trace()
        data = request.get_json()
        if 'plate' not in data:
            return missing_request('Request body should have plate field.')
        if 'owner' not in data:
            plate = PlateValidation(data['plate'], "")
        else:
            plate = PlateValidation(data['plate'], data['owner'])

        if plate.is_valid():
            if not plate.find_by_plate(data['plate']):
                plate.save_to_db()

            return valid_plate("Plate is valid")
        else:
            return invalid_plate("Plate is invalid")

class PlateList(Resource):
    def get(self):
        return jsonify([i.as_dict() for i in PlateModel.query.all()])
