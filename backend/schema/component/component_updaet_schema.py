from marshmallow import fields, post_load
from backend.schema.__base_schema import BaseSchema
from backend.entity.component_entity import ComponentEntity
from backend.schema._custome_validate.custom_types import validate_name, validate_description

class ComponentUpdateSchema(BaseSchema):
    name = fields.String(validate=validate_name)
    description = fields.String(validate=validate_description)
    image_url = fields.String()
    barcode = fields.String()
    warrantyMonth = fields.DateTime()
    device_id = fields.String()
    
    class Meta:
        fields = ('name', 'description', 'image_url', 'barcode', 'warrantyMonth', 'device_id')
        
    # @post_load
    # def to_component_entity(self, data, **kwargs):
    #     return ComponentEntity(**data)
    
    