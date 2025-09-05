"""
Módulo para interactuar con la API de datos COVID-19
"""
import pandas as pd
from sodapy import Socrata

def fetch_covid_data(departamento, limite_registros=1000):
    """
    Obtiene datos de COVID-19 desde la API de Datos Abiertos de Colombia
    
    Args:
        departamento (str): Nombre del departamento a consultar
        limite_registros (int): Número máximo de registros a obtener
    
    Returns:
        pandas.DataFrame: DataFrame con los datos obtenidos
    """
    try:
        print("Conectando con la API de Datos Abiertos...")
        
        # Cliente no autenticado (solo funciona con datasets públicos)
        client = Socrata("www.datos.gov.co", None, timeout=30)
        
        # Consulta a la API
        query = f"departamento_nom = '{departamento.upper()}'"
        results = client.get("gt2j-8ykr", where=query, limit=limite_registros)
        
        # Convertir a DataFrame
        results_df = pd.DataFrame.from_records(results)
        
        print(f"Datos obtenidos: {len(results_df)} registros")
        return results_df
        
    except Exception as e:
        print(f"Error al consultar la API: {e}")
        return None