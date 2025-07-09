from marshmallow import fields, post_dump

from backend.schema.__base_schema import BaseSchema


class CategoryResponse(BaseSchema):
    name = fields.String()
    description = fields.String()
    
    @post_dump
    def include_category(self, data, **kwargs):
        return data