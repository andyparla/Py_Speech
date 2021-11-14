import pyttsx3
import speech_recognition as sr


class PySpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 200)
        self.engine.setProperty("voice", "spanish")
        self.r = sr.Recognizer()


    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def hear_me(self):
        text = None
        with sr.Microphone() as source:
            try:
                self.r.adjust_for_ambient_noise(source, 1)
                print("Escuchando...")
                audio = self.r.listen(source)
                text = self.r.recognize_google(audio, language="es-ES")
                print(f"He entendido: {text}")
            except sr.UnknownValueError as error:
                print(f"Lo siento pero no te he escuchado: {error}")
            except KeyboardInterrupt:
                print(f"se ha cancelado el reconocimiento de voz")
        return text


if __name__ == "__main__":
    speech = PySpeech()
    """speech.speak("Te escucho")"""
    speech.hear_me()
