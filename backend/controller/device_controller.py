from flask import Blueprint, request
from backend.services.device_service import DeviceService
from backend.utils.response.response_helper import api_response

device_bp = Blueprint("device", __name__)
device_service = DeviceService()


@device_bp.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    result = device_service.create_device(data)
    return api_response(data = result)


@device_bp.route("/get-all", methods=["GET"])
def get_all():
    result = device_service.get_all_devices()
    return api_response(data = result)

@device_bp.route("/<id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    result = device_service.update_device(id, data)
    return api_response(data = result)

@device_bp.route("/<id>", methods=["DELETE"])   
def delete(id):
    result = device_service.delete_device(id)
    return api_response(data = result)

@device_bp.route("/<id>", methods=["GET"])
def get(id):
    result = device_service.get_device_by_id(id)
    return api_response(data = result)

