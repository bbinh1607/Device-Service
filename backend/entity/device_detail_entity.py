from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from ._base_entity import BaseEntity
from datetime import datetime

class DeviceDetailEntity(BaseEntity):
    __tablename__ = 'device_detail'

    device_id = Column(String, ForeignKey('device.id'), nullable=False)
    area = Column(String, nullable=False)
    buyAt = Column(DateTime, nullable=False, default=datetime.utcnow)
    warranty = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(String, nullable=True)

    # Mối quan hệ với bảng DeviceEntity
    device = relationship('DeviceEntity', backref='device_detail')
    
        