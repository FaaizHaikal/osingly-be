from fastapi import APIRouter, HTTPException
from services.translator import Translator
from schemas.translation import TranslationRequest, TranslationResponse

router = APIRouter()
translator = Translator()

@router.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    if not request.text or not str(request.text).strip():
        raise HTTPException(
            status_code=400,
            detail="Teks tidak boleh kosong"
        )
    
    try:
        result = translator.translate(request.text, request.fromOsing)
        if result["confidence"] == 0.0:
            raise HTTPException(
                status_code=500,
                detail="Maaf, gagal menerjemahkan"
            )
        return TranslationResponse(**result)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error: {str(e)}"
        )