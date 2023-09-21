import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get("/api")
async def root():
    return {"message": "Hello World"}

@app.get("/api/test")
async def root():
    return {"message": "test"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080)