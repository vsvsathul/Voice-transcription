import speech_recognition as sr
import wave

r=sr.Recognizer()
r.sample_rate=16000

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    audio=r.listen(source)
    # audio_file=sr.AudioFile("D:/Programming/Python/transcribed.wav")
    with wave.open("transcrbe.wav","wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(r.sample_rate)
        wav_file.writeframes(audio.get_wav_data())

try:
    text=r.recognize_google(audio)
    print("Transription :",text) 
except sr.UnknownValueError:
    print("Could not understand audio")

with open("Captions.txt","w") as f:
    f.write(text)
    print("Captions saved as Captions.txt")