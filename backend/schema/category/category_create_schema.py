from marshmallow import Schema, fields, post_load

from backend.schema._custome_validate.custom_types import validate_name, validate_description
from backend.entities.category_entity import CategoryEntity

class CategoryCreateSchema(Schema):
    name = fields.Str(required=True, validate=validate_name)
    description = fields.Str(required=True, validate=validate_description)
    
    @post_load
    def to_category_entity(self, data, **kwargs):
        try:
            return CategoryEntity(**data)
        except TypeError as e:
            raise (f"Error converting data to CategoryEntity: {e}")