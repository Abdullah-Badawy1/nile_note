# import requests

# def transcribe_audio(audio_file_path):
#     api_key = '46e811f9118641b89f9488849faee085'
#     endpoint = "https://api.assemblyai.com/v2/transcript"
#     headers = {
#         "authorization": api_key,
#         "content-type": "application/json"
#     }
#     audio_data = {'audio_data': open(audio_file_path, 'rb')}
#     response = requests.post(endpoint, headers=headers, files=audio_data)
    
#     if response.status_code == 200:
#         transcript_id = response.json()['id']
#         # Poll for the transcript to be completed
#         return check_transcription(transcript_id, api_key)
#     else:
#         return {"error": "Failed to transcribe audio"}

# def check_transcription(transcript_id, api_key):
#     endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
#     headers = {
#         "authorization": api_key
#     }
#     while True:
#         response = requests.get(endpoint, headers=headers)
#         if response.json()['status'] == 'completed':
#             return response.json()['text']
#         elif response.json()['status'] == 'error':
#             return {"error": "Error during transcription"}


import assemblyai as aai
import json
import codecs

# Replace with your actual AssemblyAI API key
aai.settings.api_key = "46e811f9118641b89f9488849faee085"

# URL of the file to transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"


# Transcribe the audio file
def transcribe_audio():
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL)
    if transcript.status == aai.TranscriptStatus.error:
        print(transcript.error)
    else:
        print("Transcription:")
        print(transcript.text)
        
        with open('/content/data.json', 'w', encoding='utf-8') as outfile:
            json.dump(transcript, outfile, ensure_ascii=False, indent=4)


# Add speaker labels to the transcription
def add_speaker_labels():
    config = aai.TranscriptionConfig(speaker_labels=True)
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL, config=config)
    print("\nSpeaker Labels:")
    for utterance in transcript.utterances:
        print(f"Speaker {utterance.speaker}: {utterance.text}")

# Identify topics in the transcript
def identify_topics():
    config = aai.TranscriptionConfig(iab_categories=True)
    transcript = aai.Transcriber().transcribe(FILE_URL, config=config)
    print("\nTopics in Transcript:")
    for result in transcript.iab_categories.results:
        print(result.text)
        print(f"Timestamp: {result.timestamp.start} - {result.timestamp.end}")
        for label in result.labels:
            print(f"{label.label} ({label.relevance})")
    print("\nSummary of Topics:")
    for topic, relevance in transcript.iab_categories.summary.items():
        print(f"Audio is {relevance * 100:.2f}% relevant to {topic}")

# Auto-highlight relevant sections
def auto_highlight():
    config = aai.TranscriptionConfig(auto_highlights=True)
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL, config=config)
    print("\nAuto-Highlights:")
    for result in transcript.auto_highlights.results:
        print(f"Highlight: {result.text}, Count: {result.count}, Rank: {result.rank}")

# Call the functions
transcribe_audio()
add_speaker_labels()
identify_topics()
auto_highlight()