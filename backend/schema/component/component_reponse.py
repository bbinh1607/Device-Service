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
    device_id = fields.String(dump_only=True,)
    
    
    @post_dump
    def include_device(self, data, **kwargs):
        if data is None:
            return {}
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
        
        data.pop('device_id', None)
        return data
    
    
    