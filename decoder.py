import whisper #The all new openAI whisper!
from pydub import AudioSegment

def decode(audio):
    '''
    Decodes speech to text using OpenAI Whisper. 
    In: audio: .wav file
    Out: text: str
    '''
    model = whisper.load_model("base")
    result = model.transcribe(audio)
    return result["text"]

print(decode('test.mp3'))