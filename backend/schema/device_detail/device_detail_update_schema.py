from marshmallow import Schema, fields, post_load
from backend.entities.device_detail_entity import DeviceDetailEntity

class DeviceDetailUpdateSchema(Schema):
    area = fields.String(allow_none=True)
    buyAt = fields.DateTime(allow_none=True)
    warranty = fields.DateTime(allow_none=True)
    status = fields.String(allow_none=True)
    
    class Meta:
        fields = ('area', 'buyAt', 'warranty', 'status')
        