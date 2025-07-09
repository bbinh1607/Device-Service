from backend.schema.__base_schema import BaseSchema
from marshmallow import fields, post_dump
from backend.schema.device_detail.device_detail_reponse import DeviceDetailResponse
from backend.repository.device_detail_repository import DeviceDetailRepository
from backend.repository.component_repository import ComponentRepository
from backend.schema.component.component_reponse import ComponentResponse

class ComponentDetailResponse(BaseSchema):
    component_id = fields.String(dump_only=True)
    device_detail_id = fields.String(dump_only=True)
    buy_at = fields.DateTime()
    status = fields.String()
    expirationDate = fields.DateTime()
    price = fields.Float() 
    
    @post_dump
    def include_device(self, data, **kwargs):
        device_detail_id = data.get('device_detail_id')
        component_id = data.get('component_id')
        
        if device_detail_id:
            device_detail_repository = DeviceDetailRepository()
            device_detail_entity = device_detail_repository.get_device_detail_by_id(device_detail_id)
            if device_detail_entity:
                data['device_detail'] = DeviceDetailResponse().dump(device_detail_entity)
            else:
                data['device_detail'] = None
        else:
            data['device_detail'] = None
            
        if component_id:
            component_repository = ComponentRepository()
            component_entity = component_repository.get_component_by_id(component_id)
            if component_entity:
                data['component'] = ComponentResponse().dump(component_entity)
            else:
                data['component'] = None
        else:
            data['component'] = None
            
        data.pop('device_detail_id', None)
        data.pop('component_id', None)
        return data
    