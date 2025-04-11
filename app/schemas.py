from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class ItemOut(ItemBase):
    id: int

    class Config:
        orm_mode = True


class NotificationInput(BaseModel):
    status: str
    serverCorrelationId: str
    notificationMethod: str
    objectReference: str

class NotificationResponse(BaseModel):
    serverCorrelationId: str
    received_at: str