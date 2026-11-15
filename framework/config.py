import os  # module Python qui permet notamment d'accéder aux variables d'environnement

from dotenv import load_dotenv

load_dotenv()  # Charge les variables d'environnement depuis le fichier .env


API_BASE_URL = os.getenv(
    "API_BASE_URL"
)  # Récupère la valeur de la variable d'environnement API_BASE_URL
