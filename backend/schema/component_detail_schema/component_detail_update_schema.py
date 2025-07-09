from backend.schema.__base_schema import BaseSchema
from marshmallow import fields, post_load
from backend.entities.component_detail_entity import ComponentDetailEntity

class ComponentDetailUpdateSchema(BaseSchema):
    component_id = fields.String()
    device_detail_id = fields.String()
    buy_at = fields.DateTime()
    status = fields.String()
    expirationDate = fields.DateTime()
    price = fields.Float()
    
