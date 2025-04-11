from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database
from datetime import datetime


app = FastAPI()

# Créer la base de données si elle n'existe pas encore
models.Base.metadata.create_all(bind=database.engine)

# Dépendance pour obtenir la session DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.put("/items/{item_id}", response_model=schemas.ItemOut)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db_item.name = item.name
        db_item.description = item.description
    else:
        db_item = models.Item(id=item_id, name=item.name, description=item.description)
        db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/")
def read_root():
    return {"message": "FastAPI fonctionne ! 🚀"}

@app.put("/notifications/", response_model=schemas.NotificationResponse)
def receive_notification(input: schemas.NotificationInput, db: Session = Depends(get_db)):
    notif = models.Notification(
        serverCorrelationId=input.serverCorrelationId,
        status=input.status,
        notificationMethod=input.notificationMethod,
        objectReference=input.objectReference,
        received_at=datetime.utcnow()
    )
    db.merge(notif)
    db.commit()
    return {"serverCorrelationId": input.serverCorrelationId, "received_at": notif.received_at.isoformat()}

@app.get("/notifications/{serverCorrelationId}", response_model=schemas.NotificationResponse)
def get_notification(serverCorrelationId: str, db: Session = Depends(get_db)):
    notif = db.query(models.Notification).filter_by(serverCorrelationId=serverCorrelationId).first()
    if not notif:
        raise HTTPException(status_code=404, detail="Not found")
    return {"serverCorrelationId": notif.serverCorrelationId, "received_at": notif.received_at.isoformat()}