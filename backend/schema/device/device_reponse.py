from marshmallow import fields, post_dump
from backend.schema.__base_schema import BaseSchema
from backend.schema.category.category_reponse import CategoryResponse
from backend.repository.category_repository import CategoryRepository 

class DeviceResponse(BaseSchema):
    name = fields.String()
    description = fields.String()
    barcode = fields.String()
    image_url = fields.String()
    category_id = fields.String(dump_only=True,)

    
    @post_dump
    def include_category(self, data, **kwargs):
        category_id = data.get('category_id')
        
        if category_id:
            category_repository = CategoryRepository()
            category_entity = category_repository.get_category_by_id(category_id)
            if category_entity:
                data['category'] = CategoryResponse().dump(category_entity)
            else:
                data['category'] = None
        else:
            data['category'] = None
        
        
        data.pop('category_id', None)
        return data


    