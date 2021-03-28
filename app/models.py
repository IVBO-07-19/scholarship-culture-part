from sqlalchemy import Column, Integer, Text

from app.database import Base


class Items(Base):
    __tablename__ = "t_items"

    id = Column("i_id", Integer, primary_key=True)
    fieldA = Column("tx_field_a", Text)
    fieldB = Column("tx_field_b", Text)
