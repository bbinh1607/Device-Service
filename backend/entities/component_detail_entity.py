from backend.entities._base_entity import BaseEntity
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Float
from datetime import datetime
from sqlalchemy.orm import relationship

class ComponentDetailEntity(BaseEntity):
    __tablename__ = 'component_detail'

    component_id = Column(String, ForeignKey('component.id'), nullable=False)
    device_detail_id = Column(String, ForeignKey('device_detail.id'), nullable=False)
    buy_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(String, nullable=True, default='Không sử dụng')
    expirationDate = Column(DateTime, nullable=False, default=datetime.utcnow)
    price = Column(Float, nullable=False)


    component = relationship('ComponentEntity', backref='component_detail')


    device_detail = relationship('DeviceDetailEntity', backref='component_detail')


    