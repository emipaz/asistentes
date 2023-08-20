import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEYho")

def generar_respuesta(pregunta): 
    respuesta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=pregunta,
        max_tokens=50
    )
    return respuesta.choices[0].text.strip()


def main():
    print("Bienvenido al Chatbot de OpenAI")

    while True: 
        pregunta = input("Escribe tu pregunta (o 'salir' para finalizar): ")
        
        if pregunta.lower() == 'salir': 
            print("¡Hasta luego!")
            break
        
        respuesta = generar_respuesta(pregunta)    
        print("Respuesta:", respuesta)
if __name__ == "__main__":
    main()