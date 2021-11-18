from main.speak_and_listen import PySpeech

if __name__ == "__main__":
    speech = PySpeech()
    # speech.speak("Te escucho")
    speech.transcribe()
