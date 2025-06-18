from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str
    fromOsing: bool = False  # False: ID→Osing, True: Osing→ID

class TranslationResponse(BaseModel):
    text: str
    confidence: float
