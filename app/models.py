from sqlalchemy import Column, Integer, Text, Date, Float, Boolean

from app.database import Base


class Prizes(Base):
    __tablename__ = "prizes"

    id = Column("i_id", Integer, primary_key=True)
    title = Column("tx_title", Text)
    level = Column("t_level", Text)          # уровень мероприятия (региональное, международное, всероссийское, ведомственное)
    degree = Column("t_degree", Text)        # степень участия (индивидуальное, командное)
    place = Column("i_place", Integer)       # занятое место
    date = Column("d_date", Date)            # даты мероприятий
    points = Column("f_points", Float)       # баллы
    user_id = Column("tx_userId", Text)
    id_request = Column("tx_report", Text)


class Artworks(Base):
    __tablename__ = "artworks"

    id = Column("i_id", Integer, primary_key=True)
    title = Column("tx_title", Text)
    location = Column("tx_location", Text)   # место публичного представления
    date = Column("d_date", Date)
    points = Column("f_points", Float)
    user_id = Column("tx_userId", Text)
    id_request = Column("tx_report", Text)


class Activities(Base):
    __tablename__ = "activities"

    id = Column("i_id", Integer, primary_key=True)
    title = Column("tx_title", Text)
    work = Column("tx_work", Text)
    level = Column("t_level", Text)               # уровень мероприятия (региональное, международное, всероссийское, ВУЗовское)
    date = Column("d_date", Date)
    responsible = Column("tx_responsible", Text)  # ФИО лица, подтверждающего участие
    responsiblePosition = Column("tx_responsible_position", Text)  # должность лица, подтверждающего участие
    points = Column("f_points", Float)
    status = Column("b_status", Boolean)     # в составе/не в составе творческого коллектива
    user_id = Column("tx_userId", Text)
    id_request = Column("tx_report", Text)
