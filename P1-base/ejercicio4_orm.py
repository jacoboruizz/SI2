import django
import time
import os
from dotenv import load_dotenv

# Configuracion de la base de datos
# Cargar el archivo .env
load_dotenv(dotenv_path='env')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'visaSite.settings')
django.setup()

from visaApp.models import Tarjeta

try:
    rows = list(Tarjeta.objects.all()[:1000])

     # Medir el tiempo de inicio
    start_time = time.time()

    # Realizar busquedas una a una
    for row in rows:
        id_value = row.numero
        Tarjeta.objects.get(numero=id_value)

     # Medir el tiempo de finalizacion
    end_time = time.time()

    # Mostrar los resultados
    print(f"Tiempo invertido en buscar las 1000 entradas una a una: {end_time - start_time:.6f} segundos")

except Exception as e:
    print(f"Error: {e}")
