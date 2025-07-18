from flask import Blueprint, jsonify, request
from backend.services.component_detail_service import ComponentDetailService
from backend.utils.before_request.authenticate_request import authenticate_request

component_detail_bp = Blueprint('component_detail', __name__)
component_detail_service = ComponentDetailService()

@component_detail_bp.before_request
def before_component_detail_request():
    authenticate_request()

@component_detail_bp.route('/get-all', methods=['GET'])
def get_all_component_detail():
    component_detail_entities = component_detail_service.get_all_component_detail()
    return jsonify(component_detail_entities)

@component_detail_bp.route('/<id>', methods=['GET'])
def get_component_detail_by_id(id):
    component_detail_entity = component_detail_service.get_component_detail_by_id(id)
    return jsonify(component_detail_entity)

@component_detail_bp.route('/', methods=['POST'])
def create_component_detail():
    component_detail_entity = component_detail_service.create_component_detail(request.json)
    return jsonify(component_detail_entity)

@component_detail_bp.route('/<id>', methods=['PUT'])
def update_component_detail(id):
    component_detail_entity = component_detail_service.update_component_detail(id, request.json)
    return jsonify(component_detail_entity)

@component_detail_bp.route('/<id>', methods=['DELETE'])
def delete_component_detail(id):
    component_detail_entity = component_detail_service.delete_component_detail(id)
    return jsonify(component_detail_entity)

@component_detail_bp.route('/device-detail/<device_detail_id>', methods=['GET'])
def get_component_detail_by_device_detail_id(device_detail_id):
    component_detail_entities = component_detail_service.get_component_detail_by_device_detail_id(device_detail_id)
    return jsonify(component_detail_entities)

@component_detail_bp.route('/component/<component_id>', methods=['GET'])
def get_component_detail_by_component_id(component_id):
    component_detail_entities = component_detail_service.get_component_detail_by_component_id(component_id)
    return jsonify(component_detail_entities)

    