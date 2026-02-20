import psycopg2
import time
import os
from dotenv import load_dotenv

# Configuracion de la base de datos
# Cargar el archivo .env
load_dotenv(dotenv_path='env')

# Obtener la URL de Neon
db_url = os.environ.get("DATABASE_SERVER_URL")

try:
    # Conexion a la base de datos
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()

    # Leer las primeras 1000 entradas de la tabla censo
    query_fetch_1000 = "SELECT * FROM tarjeta LIMIT 1000"
    cursor.execute(query_fetch_1000)
    rows = cursor.fetchall()

    # Preparar para las busquedas individuales
    search_query = 'SELECT * FROM tarjeta WHERE \"numero\" = %s'

     # Medir el tiempo de inicio
    start_time = time.time()

    # Realizar busquedas una a una
    for row in rows:
        id_value = row[0] # Suponiendo que la primera columna es el ID
        cursor.execute(search_query, (id_value,))
        cursor.fetchone() # Obtener la fila encontrada

     # Medir el tiempo de finalizacion
    end_time = time.time()

    # Mostrar los resultados
    print(f"Tiempo invertido en buscar las 1000 entradas una a una: {end_time - start_time:.6f} segundos")

except Exception as e:
    print(f"Error: {e}")

finally:
    # 9. Cerrar el cursor y la conexión
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()