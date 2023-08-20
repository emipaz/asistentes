# dotenv con load_dotenv carga desde ek archivo oculto .env
# las constantes o claves que necesitamos en nuestro programa

from dotenv import load_dotenv
import os

load_dotenv()

EMI = os.environ.get("EMILIANO")

print(EMI)
