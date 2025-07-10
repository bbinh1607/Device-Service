from backend.entity.component_detail_entity import ComponentDetailEntity
from backend.extensions import db
from backend.utils.handle.hande_exception import handle_exceptions_repository_class

@handle_exceptions_repository_class
class ComponentDetailRepository:
    def __init__(self):
        self.db = db.session

    def create_component_detail(self, component_detail):
        self.db.add(component_detail)
        self.db.commit()
        return component_detail
    
    def get_component_detail_by_id(self, id):
        return self.db.query(ComponentDetailEntity).filter(ComponentDetailEntity.id == id).first()
    
    def get_all_component_detail(self):
        return self.db.query(ComponentDetailEntity).all()
    
    def update_component_detail(self, id, component_detail):
        query = self.db.query(ComponentDetailEntity).filter(ComponentDetailEntity.id == id)
        query.update(component_detail)
        self.db.commit()
        entity = query.first()
        self.db.refresh(entity)
        return entity
    
    def delete_component_detail(self, id):
        component_detail = self.db.query(ComponentDetailEntity).filter(ComponentDetailEntity.id == id).first()
        if component_detail:
            self.db.delete(component_detail)
            self.db.commit()
        return component_detail
    
    def get_component_detail_by_device_detail_id(self, device_detail_id):
        return self.db.query(ComponentDetailEntity).filter(ComponentDetailEntity.device_detail_id == device_detail_id).all()
    
    def get_component_detail_by_component_id(self, component_id):
        return self.db.query(ComponentDetailEntity).filter(ComponentDetailEntity.component_id == component_id).all()