import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get("/api/getDiseaseOptions")
async def root():
    return {"message": "test"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080)