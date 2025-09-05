"""
Módulo para la interfaz de usuario y presentación de datos
"""
import pandas as pd

def get_user_input():
    """
    Obtiene la entrada del usuario para la consulta
    
    Returns:
        tuple: (departamento, limite_registros)
    """
    print("Por favor ingrese los siguientes datos para la consulta:")
    print("-" * 50)
    
    departamento = input("Departamento: ").strip()
    
    while True:
        try:
            limite = int(input("Límite de registros (máximo 1000 recomendado): "))
            if limite > 0 and limite <= 10000:
                break
            else:
                print("Por favor ingrese un número entre 1 y 10000.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    
    return departamento, limite

def display_results(df):
    """
    Muestra los resultados en formato tabular
    
    Args:
        df (pandas.DataFrame): DataFrame con los datos procesados
    """
    if df is None or df.empty:
        print("No hay datos para mostrar.")
        return
    
    print("\n" + "=" * 120)
    print("RESULTADOS DE LA CONSULTA - CASOS COVID-19")
    print("=" * 120)
    
    # Formatear el DataFrame para mejor presentación
    formatted_df = df.copy()
    
    # Mostrar las primeras filas con formato
    with pd.option_context('display.max_rows', None, 
                          'display.max_columns', None,
                          'display.width', None,
                          'display.colheader_justify', 'center'):
        print(formatted_df.to_string(index=False))
    
    print(f"\nTotal de registros encontrados: {len(df)}")
    print("=" * 120)