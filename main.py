import uvicorn
from fastapi import FastAPI
app = FastAPI()

<<<<<<< HEAD
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def test():
=======
@app.get("/api/test")
async def root():
>>>>>>> main
    return {"message": "test"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080)