from marshmallow import fields, post_dump
from backend.schema.__base_schema import BaseSchema
from backend.client.file_service_client import FileServiceClient

class ComponentResponse(BaseSchema):
    name = fields.String()
    description = fields.String()
    image_url = fields.String()
    barcode = fields.String()
    warrantyMonth = fields.DateTime()
    
    file = fields.Raw( dump_only=True)
    device_id = fields.String();
    
    
    @post_dump
    def include_file(self, data, **kwargs):
        if 'image_url' in data and data['image_url'] is not None:
            file_data = FileServiceClient().get_file_by_id(data['image_url'])
            
            data['file'] = file_data

            del data['image_url']          
        
        return data


    
    