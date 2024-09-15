from flask import Blueprint, jsonify, request
from npc_manager.database import db
from npc_manager.models.car import Car

blueprint = Blueprint('cars', __name__)

@blueprint.route('/cars', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    car_list = []
    for car in cars:
        car_data = {
            'id': car.id,
            'model': car.model,
            'owner_id': car.owner_id
        }
        car_list.append(car_data)
        
    return jsonify(car_list)
    