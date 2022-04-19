from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.database import Base


class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey(
        "users.id"
    ), nullable=False)
    clinic_id = Column(Integer, nullable=False)
    schedule = Column(DateTime, nullable=False)
    fees_paid = Column(Boolean, server_default='False', nullable=False)
    is_completed = Column(Boolean, server_default='False', nullable=False)
    is_skipped = Column(Boolean, server_default='False', nullable=False)
    when_skipped = Column(DateTime, nullable=True)
    is_cancelled = Column(Boolean, server_default='False', nullable=False)
    when_cancelled = Column(DateTime, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


#! SCHEDULE DATETIME EXAMPLE 2018-12-19 09:26:03.478039