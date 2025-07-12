import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

class TranscribeRequest(BaseModel):
    video_id: str

@app.post("/transcribe")
def transcribe(request: TranscribeRequest):
    try:
        proxy_url = os.getenv("YT_PROXY")  # Exemplo: http://usuario:senha@proxy.decodo.com:porta
        proxies = [proxy_url] if proxy_url else None
        transcript = YouTubeTranscriptApi.get_transcript(
            request.video_id,
            proxies=proxies
        )
        transcription_text = "\n".join(entry['text'] for entry in transcript)
        return {"video_id": request.video_id, "transcription": transcription_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao obter transcrição: {e}")
