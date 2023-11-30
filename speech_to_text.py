import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import subprocess as sp
import ffmpeg_downloader as ffdl


def speech_to_text_from_file(file_path):
    sp.run([ffdl.ffmpeg_path, '-i', file_path, 'answer_audio\\' + file_path[-8:-4] + '.wav'])
    recognizer = sr.Recognizer()
    try:
        file_path = 'answer_audio\\' + file_path[-8:-4] + '.wav'
        # Load the audio file
        with sr.AudioFile(file_path) as source:
            print("Processing audio file...")
            audio = recognizer.record(source)

        # Use Google Web Speech API to convert audio to text
        text = recognizer.recognize_google(audio)
        # print("Text from audio file: {}".format(text))
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Error connecting to Google Speech Recognition service; {0}".format(e))
    except Exception as e:
        print("Error: {0}".format(e))

        
# print(speech_to_text_from_file("answer_audio\\kesu1407@gmail.comans1.wav"))


