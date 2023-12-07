from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import sys

import uvicorn
sys.path.append(r'C:/Users/tzolz/Desktop/PythonforDA')
from APP.API.routers import drug_risk


app = FastAPI(title="Drug consumption project")

app.include_router(drug_risk.router)

@app.get("/")
def root():
    return {"message":"API is running well"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
