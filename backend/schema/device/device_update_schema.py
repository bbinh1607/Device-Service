from marshmallow import Schema, fields, post_load
from backend.schema.__base_schema import BaseSchema
from backend.entities.device_entity import DeviceEntity


class DeviceUpdateSchema(BaseSchema):
    name = fields.String(required=False)
    description = fields.String(required=False)
    image_url = fields.String(required=False)
    barcode = fields.String(required=False)
    category_id = fields.Integer(required=False)

    class Meta:
        fields = ('name', 'description', 'image_url', 'barcode', 'category_id')
        
    @post_load
    def to_device_entity(self, data, **kwargs):
        try:
            return DeviceEntity(**data)
        except TypeError as e:
            raise ValueError(f"Error converting data to DeviceEntity: {e}")