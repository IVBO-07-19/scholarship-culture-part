from sqlalchemy import Column, Integer, Text, Date, Float, Boolean

from app.database import Base


class Prizes(Base):
    __tablename__ = "prizes"

    id = Column("i_id", Integer, primary_key=True)
    title = Column("tx_title", Text)
    level = Column("i_level", Integer)
    degree = Column("i_degree", Integer)
    place = Column("i_place", Integer)
    date = Column("d_date", Date)
    points = Column("f_points", Float)


class Artworks(Base):
    __tablename__ = "artworks"

    id = Column("i_id", Integer, primary_key=True)
    title = Column("tx_title", Text)
    location = Column("tx_location", Text)
    date = Column("d_date", Date)
    points = Column("f_points", Float)


class Activities(Base):
    __tablename__ = "activities"

    id = Column("i_id", Integer, primary_key=True)
    title = Column("tx_title", Text)
    work = Column("tx_work", Text)
    level = Column("i_level", Integer)
    date = Column("d_date", Date)
    responsible = Column("tx_responsible", Text)
    responsiblePosition = Column("tx_responsible_position", Text)
    points = Column("f_points", Float)
    status = Column("b_status", Boolean)
