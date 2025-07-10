from backend.entity._base_entity import BaseEntity
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class ComponentDeviceEntity(BaseEntity):
    __tablename__ = 'component_device'

    # Khóa ngoại liên kết tới ComponentEntity và DeviceEntity
    component_id = Column(String, ForeignKey('component.id'), primary_key=True)
    device_id = Column(String, ForeignKey('device.id'), primary_key=True)


    # Mối quan hệ với ComponentEntity
    component = relationship('ComponentEntity', backref='device_components')

    # Mối quan hệ với DeviceEntity
    device = relationship('DeviceEntity', backref='component_devices')
