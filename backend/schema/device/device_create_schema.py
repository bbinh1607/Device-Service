from marshmallow import fields, post_load
from backend.entity.device_entity import DeviceEntity
from backend.schema._custome_validate.custom_types import validate_name, validate_description
from backend.schema.__base_schema import BaseSchema

class DeviceCreateSchema(BaseSchema):
    name = fields.String(required=True, validate=validate_name)
    description = fields.String(required=True, validate=validate_description)
    barcode = fields.String(allow_none=True)
    image_url = fields.String()
    category_id = fields.String(required=True)

    class Meta:
        fields = ('name', 'description', 'barcode', 'image_url', 'category_id')
        
    @post_load
    def to_device_entity(self, data, **kwargs):
        try:
            return DeviceEntity(**data)
        except TypeError as e:
            raise ValueError(f"Error converting data to DeviceEntity: {e}")
