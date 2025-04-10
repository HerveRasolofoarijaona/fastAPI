from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database

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
