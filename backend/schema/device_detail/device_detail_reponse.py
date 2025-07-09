from marshmallow import fields, post_dump
from backend.schema.__base_schema import BaseSchema
from backend.schema.device.device_reponse import DeviceResponse
from backend.repository.device_repository import DeviceRepository

class DeviceDetailResponse(BaseSchema):
    device_id = fields.String(dump_only=True)
    area = fields.String()
    buyAt = fields.DateTime()
    warranty = fields.DateTime()
    status = fields.String()
    
        
    @post_dump
    def include_device(self, data, **kwargs):
        device_id = data.get('device_id')
        if device_id:
            device_repository = DeviceRepository()
            device_entity = device_repository.get_device_by_id(device_id)
            if device_entity:
                data['device'] = DeviceResponse().dump(device_entity)
            else:
                data['device'] = None
        else:
            data['device'] = None
        return data
    
    