from backend.schema.__base_schema import BaseSchema
from marshmallow import fields, post_load
from backend.entity.component_detail_entity import ComponentDetailEntity

class ComponentDetailCreateSchema(BaseSchema):
    component_id = fields.String(required=True)
    device_detail_id = fields.String()
    buy_at = fields.DateTime()
    status = fields.String()
    expirationDate = fields.DateTime()
    price = fields.Float()
    
    @post_load
    def to_component_detail_entity(self, data, **kwargs):
        try:
            return ComponentDetailEntity(**data)
        except TypeError as e:
            raise ValueError(f"Error converting data to ComponentDetailEntity: {e}")
    