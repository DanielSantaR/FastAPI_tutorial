from endpoints import app
from fastapi import FastAPI
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
