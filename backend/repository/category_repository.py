from backend.extensions import db
from backend.entity.category_entity import CategoryEntity
from backend.utils.handle.hande_exception import handle_exceptions_repository_class

@handle_exceptions_repository_class
class CategoryRepository:
    def __init__(self):
        self.db = db.session
        
    def create_category(self, category):
        self.db.add(category)
        self.db.commit()
        return category
    
    def get_category_by_id(self, id):
        category = self.db.query(CategoryEntity).filter(CategoryEntity.id == id).first()
        return category
        
    def get_all_category(self):
        list_category = self.db.query(CategoryEntity).all()
        return list_category
    
    def update_category(self, id, category):
        query = self.db.query(CategoryEntity).filter(CategoryEntity.id == id)
        query.update(category)
        self.db.commit()
        entity = query.first()
        self.db.refresh(entity)
        return entity

    
    def delete_category(self, id):
        category = self.db.query(CategoryEntity).filter(CategoryEntity.id == id).first()
        if category:
            self.db.delete(category)
            self.db.commit()
        return category
    