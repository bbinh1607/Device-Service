from flask import Blueprint, request
from backend.services.category_service import CategoryService
from backend.utils.response.response_helper import api_response

category_bp = Blueprint("category", __name__)
category_service = CategoryService()

@category_bp.route("/create", methods=["POST"])
def create_category():
    data = request.get_json()
    result = category_service.create_category(data)
    return api_response(data=result)
   
@category_bp.route("/get-all", methods=["GET"])
def get_all():
    result = category_service.get_all()
    return api_response(data=result)

@category_bp.route("/<id>", methods=["GET"])
def get_by_id(id):
    result = category_service.get_by_id(id)
    return api_response(data=result)

@category_bp.route("/<id>", methods=["DELETE"])
def delete_by_id(id):
    result = category_service.delete(id)
    return api_response(message=result)

