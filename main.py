from fastapi import FastAPI
from routes.translate import router as translate_router

app = FastAPI(title="Osing Translator API")

app.include_router(translate_router, prefix="/api")

@app.get("/")
async def health_check():
    return {"status": "healthy"}