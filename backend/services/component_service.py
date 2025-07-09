from backend.repository.component_repository import ComponentRepository
from backend.schema.component.component_create_schema import ComponentCreateSchema
from backend.schema.component.component_reponse import ComponentResponse
from backend.schema.component.component_updaet_schema import ComponentUpdateSchema
from backend.error.business_errors import ComponentNotFound
from backend.utils.handle.hande_exception import handle_exceptions_class

@handle_exceptions_class
class ComponentService:
    def __init__(self):
        self.component_repository = ComponentRepository()
        
    def create_component(self, component):
        component = ComponentCreateSchema().load(component)
        component = self.component_repository.create_component(component)
        return ComponentResponse().dump(component)
    
    def get_component_by_id(self, id):
        component = self.component_repository.get_component_by_id(id)
        return ComponentResponse().dump(component)
    
    def update_component(self, id, component):
        component = ComponentUpdateSchema().load(component)
        component_entity = self.component_repository.get_component_by_id(id)
        if not component_entity:
            raise ComponentNotFound()
        component = self.component_repository.update_component(id, component)
        return ComponentResponse().dump(component)
    
    def delete_component(self, id):
        component_entity = self.component_repository.get_component_by_id(id)
        if not component_entity:
            raise ComponentNotFound()
        component = self.component_repository.delete_component(id)
        return ComponentResponse().dump(component)
        
    def get_all_components(self):
        components = self.component_repository.get_all_components()
        return ComponentResponse(many=True).dump(components)
        
        
        