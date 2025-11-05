from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from LeIA import SentimentIntensityAnalyzer

app = FastAPI()
analyzer = SentimentIntensityAnalyzer()

class SentimentRequest(BaseModel):
    text: str

    @field_validator('text')
    def validate_text_length(cls, v):
        max_length = 280
        if not v or len(v.strip()) == 0:
            raise ValueError("O texto não pode ser vazio.")
        if len(v) > max_length:
            raise ValueError(f"O texto deve conter no máximo {max_length} caracteres.")
        return v

@app.post("/sentiment")
async def analyze_sentiment(request: SentimentRequest):
    try:
        scores = analyzer.polarity_scores(request.text)
        return {"scores": scores}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
