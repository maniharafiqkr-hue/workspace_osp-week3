from fastapi import FastAPI
from pydantic import BaseModel
from profanity import mask_profanity

app = FastAPI(title="Profanity Masking API")

class TextRequest(BaseModel):
    text: str

@app.post("/mask")
def mask_text(request: TextRequest):
    masked = mask_profanity(request.text)
    return {"masked_text": masked}
