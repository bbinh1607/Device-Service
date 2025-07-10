from marshmallow import fields, post_load
from backend.schema.__base_schema import BaseSchema
from backend.schema._custome_validate.custom_types import validate_name, validate_description
from backend.entity.component_entity import ComponentEntity

class ComponentCreateSchema(BaseSchema):
    name = fields.String(required=True, validate=validate_name)
    description = fields.String(required=True, validate=validate_description)
    image_url = fields.String()
    barcode = fields.String()
    warrantyMonth = fields.DateTime()
    device_id = fields.String(required=True)
    
    class Meta:
        fields = ('name', 'description', 'image_url', 'barcode', 'warrantyMonth', 'device_id')
    
    @post_load
    def to_component_entity(self, data, **kwargs):
        try:
            return ComponentEntity(**data)
        except TypeError as e:
            raise ValueError(f"Error converting data to ComponentEntity: {e}")
    