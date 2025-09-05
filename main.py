"""
Módulo principal de la aplicación de consulta de datos COVID-19
"""
from ui.user_interface import get_user_input, display_results
from api.covid_api import fetch_covid_data
from utils.data_utils import process_covid_data

def main():
    """Función principal que orquesta toda la aplicación"""
    print("=== CONSULTA DE DATOS COVID-19 EN COLOMBIA ===")
    print("Fuente: Portal Nacional de Datos Abiertos")
    print()
    
    # Obtener entrada del usuario
    departamento, limite = get_user_input()
    
    # Fetch data from API
    print(f"\nConsultando datos para {departamento}...")
    raw_data = fetch_covid_data(departamento, limite)
    
    if raw_data is not None and len(raw_data) > 0:
        # Procesar datos
        processed_data = process_covid_data(raw_data)
        
        # Mostrar resultados
        display_results(processed_data)
    else:
        print("No se encontraron datos para los criterios especificados.")

if __name__ == "__main__":
    main()
