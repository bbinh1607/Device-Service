from flask import Blueprint, request
from backend.services.component_service import ComponentService
from backend.utils.response.response_helper import api_response
from backend.utils.before_request.authenticate_request import authenticate_request

component_bp = Blueprint('component', __name__)

@component_bp.before_request
def before_component_request():
    authenticate_request()

@component_bp.route('/create', methods=['POST'])
def create_component():
    data = request.get_json()
    result = ComponentService().create_component(data)
    return api_response(data = result)

@component_bp.route('/get-all', methods=['GET'])
def get_all_components():
    result = ComponentService().get_all_components()
    return api_response(data = result)

@component_bp.route('/<id>', methods=['GET'])
def get_component(id):
    result = ComponentService().get_component_by_id(id)
    return api_response(data = result)

@component_bp.route('/<id>', methods=['PUT'])
def update_component(id):
    data = request.get_json()
    result = ComponentService().update_component(id, data)
    return api_response(data = result)

@component_bp.route('/<id>', methods=['DELETE'])
def delete_component(id):
    result = ComponentService().delete_component(id)
    return api_response(data = result)




