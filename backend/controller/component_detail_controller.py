from flask import Blueprint, jsonify, request
from backend.services.component_detail_service import ComponentDetailService
from backend.utils.before_request.authenticate_request import authenticate_request
from backend.utils.response.response_helper import api_response

component_detail_bp = Blueprint('component_detail', __name__)
component_detail_service = ComponentDetailService()

@component_detail_bp.before_request
def before_component_detail_request():
    authenticate_request()

@component_detail_bp.route('/get-all', methods=['GET'])
def get_all_component_detail():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    component_id = request.args.get("component_id")
    device_detail_id = request.args.get("device_detail_id")
    status = request.args.get("status")
    buy_at = request.args.get("buy_at")

    result = component_detail_service.get_all_component_detail(
        page=page,
        limit=limit,
        component_id=component_id,
        device_detail_id=device_detail_id,
        status=status,
        buy_at=buy_at,
    )

    return api_response(data=result)

@component_detail_bp.route('/<id>', methods=['GET'])
def get_component_detail_by_id(id):
    component_detail_entity = component_detail_service.get_component_detail_by_id(id)
    return api_response(data=component_detail_entity)

@component_detail_bp.route('/', methods=['POST'])
def create_component_detail():
    component_detail_entity = component_detail_service.create_component_detail(request.json)
    return api_response(data=component_detail_entity)

@component_detail_bp.route('/<id>', methods=['PUT'])
def update_component_detail(id):
    component_detail_entity = component_detail_service.update_component_detail(id, request.json)
    return api_response(data=component_detail_entity)

@component_detail_bp.route('/<id>', methods=['DELETE'])
def delete_component_detail(id):
    component_detail_entity = component_detail_service.delete_component_detail(id)
    return api_response(data=component_detail_entity)


    