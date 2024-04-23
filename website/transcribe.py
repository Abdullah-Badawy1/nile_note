import speech_recognition as sr

# Function to transcribe audio
def transcribe_audio(audio_file_path):
    # Initialize the recognizer
    r = sr.Recognizer()
    
    # Use the audio file in the context manager
    with sr.AudioFile(audio_file_path) as source:
        # This helps the recognizer calibrate for the noise level of the audio
        r.adjust_for_ambient_noise(source)
        audio_data = r.record(source)
        
        # Add error handling to get more information about what might be going wrong
        try:
            # Transcribe audio using Google Web Speech API
            text = r.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Replace with the path to your actual audio file
audio_file_path = "path_to_your_audio_file.wav"

# Call the function and print the result
transcribed_text = transcribe_audio(audio_file_path)
if transcribed_text:
    print(transcribed_text)
