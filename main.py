"""
Profanity Masking API - TADD Web Service
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from profanity import ProfanityFilter

app = FastAPI(
    title="Profanity Masking API",
    description="Educational TADD exercise API",
    version="1.0.0"
)

# Fixes Smell 5 (DIP): We instantiate our filter class here. 
# In the future, we could easily swap this with a different filter class.
profanity_filter = ProfanityFilter()

class TextRequest(BaseModel):
    text: str

class TextResponse(BaseModel):
    masked_text: str

@app.post("/mask", response_model=TextResponse)
def mask_text(request: TextRequest) -> TextResponse:
    """
    Mask profanity in input text.
    
    - Preserves first letter, masks rest with *
    - Case-insensitive banned words: damn, hell, crap
    - Returns original text if no profanity found
    """
    try:
        masked = profanity_filter.mask_profanity(request.text)
        return TextResponse(masked_text=masked)
    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid input: text cannot be None")