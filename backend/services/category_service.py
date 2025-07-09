from backend.repository.category_repository import CategoryRepository
from backend.error.business_errors import CategoryNotFound, CategoryNameExists
from backend.schema.category.category_create_schema import CategoryCreateSchema
from backend.schema.category.category_reponse import CategoryResponse
from backend.utils.handle.hande_exception import handle_exceptions_class

@handle_exceptions_class
class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()
        
    def create_category(self, category):
        category = CategoryCreateSchema().load(category)
        category = self.category_repository.create_category(category)
        return CategoryResponse().dump(category)
    
    def get_by_id(self, id):
        category = self.category_repository.get_category_by_id(id)
        if not category:
            raise CategoryNotFound()
        result = CategoryResponse().dump(category)
        return result
    
    def get_all(self):
        categories = self.category_repository.get_all_category()
        return CategoryResponse(many=True).dump(categories)
    
    def delete_by_id(self, id):
        category = self.category_repository.get_category_by_id(id)
        if not category:
            raise CategoryNotFound()
        self.category_repository.delete_category(id)
        return "Đã xóa thành công"