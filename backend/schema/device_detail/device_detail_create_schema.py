from marshmallow import Schema, fields, post_load
from backend.entity.device_detail_entity import DeviceDetailEntity

class DeviceDetailCreateSchema(Schema):
    device_id = fields.String(required=True)
    area = fields.String(allow_none=True)
    buyAt = fields.DateTime(allow_none=True)
    warranty = fields.DateTime(allow_none=True)
    status = fields.String(allow_none=True)
    
    class Meta:
        fields = ('device_id', 'area', 'buyAt', 'warranty', 'status')
        
    
    @post_load
    def to_device_detail_entity(self, data, **kwargs):
        try:
            return DeviceDetailEntity(**data)
        except TypeError as e:
            raise ValueError(f"Error converting data to DeviceDetailEntity: {e}")
    
    
    