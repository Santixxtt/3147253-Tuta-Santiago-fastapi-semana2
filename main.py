from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import hashlib
import models, schemas, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)
