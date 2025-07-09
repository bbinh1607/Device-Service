from backend.entities._base_entity import BaseEntity
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class ComponentEntity(BaseEntity):
    __tablename__ = 'component'

    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    barcode = Column(String, nullable=True)
    warrantyMonth = Column(DateTime, nullable=True)
    device_id = Column(String, ForeignKey('device.id'), nullable=False)
    
    device = relationship('DeviceEntity', backref='components')
    
    