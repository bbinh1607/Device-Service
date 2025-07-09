from backend.repository.device_repository import DeviceRepository
from backend.repository.category_repository import CategoryRepository
from backend.schema.device.device_reponse import DeviceResponse
from backend.schema.device.device_create_schema import DeviceCreateSchema
from backend.schema.device.device_update_schema import DeviceUpdateSchema
from backend.error.business_errors import DeviceNotFound
from backend.utils.handle.hande_exception import handle_exceptions_class

@handle_exceptions_class
class DeviceService:
    def __init__(self):
        self.device_repository = DeviceRepository()
        self.category_repository = CategoryRepository()
        

    def create_device(self, data):
        device =  DeviceCreateSchema().load(data)
        if device.category_id is not None:
            self.category_repository.get_category_by_id(device.category_id)
        device = self.device_repository.create_device(device)
        return DeviceResponse().dump(device)
        
    def get_device_by_id(self, id):
        device = self.device_repository.get_device_by_id(id)
        return DeviceResponse().dump(device)
    
    def get_all_devices(self):
        devices = self.device_repository.get_all_devices()
        return DeviceResponse(many=True).dump(devices)
    
    def update_device(self, id , data):
        device = self.device_repository.get_device_by_id(id)
        if device is None:
            raise DeviceNotFound()
        device_update = DeviceUpdateSchema().load(data)
        device = self.device_repository.update_device(id, device_update)
        return DeviceResponse().dump(device)
    
    def delete_device(self, id):
        device = self.device_repository.get_device_by_id(id)
        if device is None:
            raise DeviceNotFound()
        device = self.device_repository.delete_device(id)
        return DeviceResponse().dump(device)
        