from marshmallow import fields, post_dump, pre_dump , post_load
from backend.schema.__base_schema import BaseSchema
from backend.schema.category.category_reponse import CategoryResponse

class DeviceResponse(BaseSchema):
    name = fields.String()
    description = fields.String()
    barcode = fields.String()
    image_url = fields.String()
    
    category = fields.Nested(CategoryResponse, dump_only=True)

    @pre_dump
    def handle_object(self, data, **kwargs):
        return data

    @post_dump
    def include_category(self, data, **kwargs):
        return data
