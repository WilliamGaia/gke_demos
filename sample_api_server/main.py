# main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def get_headers(request: Request):
    return JSONResponse(dict(request.headers))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}