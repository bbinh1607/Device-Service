from sqlalchemy import Column, String
from ._base_entity import BaseEntity

class FileEntity(BaseEntity):
    __tablename__ = 'files'

    name = Column(String, nullable=False)
    path = Column(String, nullable=False)
    type = Column(String, nullable=False)
    folder = Column(String, nullable=False)