from device_service.backend.repository.device_detail_repository import DeviceDetailRepository
from backend.schema.device_detail.device_detail_create_schema import DeviceDetailCreateSchema
from backend.schema.device_detail.device_detail_reponse import DeviceDetailResponse
from backend.schema.device_detail.device_detail_update_schema import DeviceDetailUpdateSchema
from backend.utils.handle.hande_exception import handle_exceptions_class

@handle_exceptions_class
class DeviceDetailService:
    def __init__(self):
        self.device_detail_repository = DeviceDetailRepository()
        
    def create_device_detail(self, data):
        device_detail_schema = DeviceDetailCreateSchema().load(data)
        device_detail_entity = self.device_detail_repository.create_device_detail(device_detail_schema)
        return DeviceDetailResponse().dump(device_detail_entity)
    
    def get_device_detail_by_id(self, id):
        device_detail_entity = self.device_detail_repository.get_device_detail_by_id(id)
        return DeviceDetailResponse().dump(device_detail_entity)
    
    def update_device_detail(self, id, device_detail_data):
        device_detail_schema = DeviceDetailUpdateSchema().load(device_detail_data)
        device_detail_entity = self.device_detail_repository.update_device_detail(id, device_detail_schema)
        return DeviceDetailResponse().dump(device_detail_entity)
    
    def delete_device_detail(self, id):
        device_detail_entity = self.device_detail_repository.delete_device_detail(id)
        return DeviceDetailResponse().dump(device_detail_entity)
    
    def get_all_device_detail(self):
        device_detail_entities = self.device_detail_repository.get_all_device_detail()
        return DeviceDetailResponse(many=True).dump(device_detail_entities)
        
