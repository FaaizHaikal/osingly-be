from fastapi import FastAPI
from routes.translate import router as translate_router
from services.model_loader import model_loader

app = FastAPI(title="Osing Translator API")

app.include_router(translate_router, prefix="/api")

@app.get("/")
async def health_check():
    return {"status": "healthy"}