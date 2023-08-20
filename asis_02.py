import speech_recognition as sr
import pywhatkit
import pyttsx3
import wikipedia
import datetime
# from pygame import mixer
# import keyboard

engine = pyttsx3.init()
escucha = sr.Recognizer()

voz = engine.getProperty("voices")
engine.setProperty("voice", voz[0].id)
engine.setProperty("rate", 145)
name = "compu"

def talk(text):
    engine.say(text)
    engine.runAndWait()
   

def listen():
    
        with sr.Microphone() as source:
            print("Microfono abierto:")
            pc = escucha.listen(source, timeout = 2)
            rec = escucha.recognize_google(pc, language="es").lower()
            print(rec)
            if name in rec:
                rec = rec.replace(name,"")
                print("te escucho")
        return rec
                  
        
def main():
    while True:
        try:
            rec = listen()
            print(rec)
        except:
            continue
        if "reproduce" in rec:
            music = rec.replace("reproduce","")
            print("abriendo youtube en :", music)
            talk("abriendo youtube en :"+ music)
            pywhatkit.playonyt(music)
        elif "buscar" in rec or "buscar" in rec:
            search = rec.replace("buscar","")
            wikipedia.set_lang("es")
            try:
                wiki = wikipedia.summary(search, 5)
            except Exception as e:
                print (e)
                continue
            else:
                print(search + ": "+ wiki)
                talk(wiki)
        elif str.startswith(rec, "salir") :
            print("gracias por usar el asistente")
            talk("Hasta la proxima")
            break
        

if __name__ == "__main__":
    main()