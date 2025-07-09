from sqlalchemy import Column, String
from ._base_entity import BaseEntity


class CategoryEntity(BaseEntity):
    __tablename__ = 'categorie'

    name = Column(String, nullable=False,unique=True )
    description = Column(String, nullable=True)