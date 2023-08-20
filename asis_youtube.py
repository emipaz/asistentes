import speech_recognition as sr
import pywhatkit
import pyttsx3

engine = pyttsx3.init()
escucha = sr.Recognizer()

voz = engine.getProperty("voices")
engine.setProperty("voice", voz[0].id)
name = "compu"

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Microfono abierto:")
            pc = escucha.listen(source)
            rec = escucha.recognize_google(pc).lower()
            if name in rec:
                rec = rec.replace(name,"")
    except Exception as e:
        print(e)
        pass
    return rec

def main():
    rec = listen()
    if "reproduce" in rec:
        music = rec.replace("reproduce","")
        print("abriendo youtube en :", music)
        talk("abriendo youtube en :"+ music)
        pywhatkit.playonyt(music)


if __name__ == "__main__":
    main()



