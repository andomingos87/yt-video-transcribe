from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

class TranscribeRequest(BaseModel):
    video_id: str

@app.post("/transcribe")
def transcribe(request: TranscribeRequest):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(request.video_id)
        # Junta todos os textos em uma string única
        transcription_text = "\n".join(entry['text'] for entry in transcript)
        return {"video_id": request.video_id, "transcription": transcription_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao obter transcrição: {e}")
