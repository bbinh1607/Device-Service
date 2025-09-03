from backend.entity.component_entity import ComponentEntity
from backend.extensions import db
from backend.utils.handle.hande_exception import handle_exceptions_repository_class

@handle_exceptions_repository_class
class ComponentRepository:
    def __init__(self):
        self.db = db.session
        
    def create_component(self, component):
        self.db.add(component)
        self.db.commit()
        return component
    
    def get_component_by_id(self, id):
        component = self.db.query(ComponentEntity).filter(ComponentEntity.id == id).first()
        return component
        
    def get_all_components(self, page=1, limit=10, name=None, barcode=None, device_id=None):
        query = self.db.query(ComponentEntity)

        if name:
            query = query.filter(ComponentEntity.name.ilike(f"%{name}%"))
        if barcode:
            query = query.filter(ComponentEntity.barcode.ilike(f"%{barcode}%"))
        if device_id:
            query = query.filter(ComponentEntity.device_id == device_id)

        total = query.count()

        results = query.order_by(ComponentEntity.created_at.desc()) \
                    .offset((page - 1) * limit) \
                    .limit(limit).all()

        return results, total
        
    def update_component(self, id, component: dict):
        query = self.db.query(ComponentEntity).filter(ComponentEntity.id == id)
        query.update(component)
        self.db.commit()
        entity = query.first()
        self.db.refresh(entity)
        return entity

            
    def delete_component(self, id):
        component = self.db.query(ComponentEntity).filter(ComponentEntity.id == id).first()
        self.db.delete(component)
        self.db.commit()
        return component

        
        