from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.db import get_db

from app.core.config import settings

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World",
            "db":settings.SQLALCHEMY_DATABASE_URL}

@app.get("/db-check")
def check_database(db: Session = Depends(get_db)):
    try:
        # 간단한 쿼리 실행
        result = db.execute(text("SELECT 1"))
        if result.scalar() == 1:
            return {"status": "success", "message": "Database connection is successful"}
        else:
            raise HTTPException(status_code=500, detail="Unexpected database response")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

