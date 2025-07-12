from youtube_transcript_api import YouTubeTranscriptApi

# Substitua pelo ID do vídeo do YouTube que deseja transcrever
video_id = "fl-0UVFjqs0"  # Exemplo

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    
    # Criar um arquivo e salvar a transcrição
    with open(f"{video_id}_transcription.txt", "w", encoding="utf-8") as file:
        for entry in transcript:
            file.write(entry['text'] + "\n")

    print(f"Transcrição salva em {video_id}_transcription.txt")

except Exception as e:
    print(f"Erro ao obter transcrição: {e}")
