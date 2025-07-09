from backend.extensions import db
from backend.entities.device_detail_entity import DeviceDetailEntity
from backend.utils.handle.hande_exception import handle_exceptions_repository_class

@handle_exceptions_repository_class
class DeviceDetailRepository:
    def __init__(self):
        self.db = db.session

    def create_device_detail(self, device_detail):
        self.db.add(device_detail)
        self.db.commit()
        return device_detail
    
    def get_device_detail_by_device_id(self, device_id):
        return self.db.query(DeviceDetailEntity).filter(DeviceDetailEntity.device_id == device_id).first()

    def update_device_detail(self, id, device_detail): 
        query = self.db.query(DeviceDetailEntity).filter(DeviceDetailEntity.id == id)
        query.update(device_detail)
        self.db.commit()
        entity = query.first()
        self.db.refresh(entity)
        return entity

    
    def delete_device_detail(self, id):
        device_detail_data = self.db.query(DeviceDetailEntity).filter(DeviceDetailEntity.id == id).first()
        self.db.delete(device_detail_data)
        self.db.commit()
        return device_detail_data
    
    
    def get_all_device_detail(self):
        return self.db.query(DeviceDetailEntity).all()
    
    
    def get_device_detail_by_id(self, id):
        return self.db.query(DeviceDetailEntity).filter(DeviceDetailEntity.id == id).first()
