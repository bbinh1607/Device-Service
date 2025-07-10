from marshmallow import fields, post_dump
from backend.schema.__base_schema import BaseSchema
from backend.schema.device.device_reponse import DeviceResponse
from backend.repository.device_repository import DeviceRepository

class ComponentResponse(BaseSchema):
    name = fields.String()
    description = fields.String()
    image_url = fields.String()
    barcode = fields.String()
    warrantyMonth = fields.DateTime()
    
    device = fields.Nested(DeviceResponse, dump_only=True)
    

    
    