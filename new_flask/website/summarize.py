import requests
#from transcribe import transcript
import assemblyai as aai

aai.settings.api_key = "46e811f9118641b89f9488849faee085"

audio_url = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

config = aai.TranscriptionConfig(
  summarization=True,
  summary_model=aai.SummarizationModel.informative,
  summary_type=aai.SummarizationType.bullets
)

transcript = aai.Transcriber().transcribe(audio_url, config)

print(transcript.summary)



# def summarize_text(transcript):
#     api_key = '46e811f9118641b89f9488849faee085'
#     endpoint = "https://api.assemblyai.com/v2/summarize"
#     headers = {
#         "authorization": api_key,
#         "content-type": "application/json"
#     }
#     json = {
#         "text": transcript
#     }
#     response = requests.post(endpoint, json=json, headers=headers)
    
#     if response.status_code == 200:
#         return response.json()['summary']
#     else:
#         return {"error": "Failed to summarize text"}

