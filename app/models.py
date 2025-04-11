from sqlalchemy import Column, Integer, String,DateTime
from .database import Base
from datetime import datetime

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)

class Notification(Base):
    __tablename__ = "notifications"

    serverCorrelationId = Column(String, primary_key=True, index=True)
    status = Column(String)
    notificationMethod = Column(String)
    objectReference = Column(String)
    received_at = Column(DateTime, default=datetime.utcnow)


