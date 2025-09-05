"""
Módulo de utilidades para procesamiento de datos
"""

# Diccionario CODIGOS_DANE
# Fuente: DANE - División político-administrativa de Colombia (DIVIPOLA)
CODIGOS_DANE = {
    "11001": "Bogotá D.C.",
    "05001": "Medellín",
    "05002": "Abejorral",
    "05004": "Abriaquí",
    "99773": "Tarapacá",
    "76001": "Cali",
    "73001": "Ibagué",
    "68001": "Bucaramanga",
    "54001": "Cúcuta",
    "52001": "Pasto",
    "5001": "Villavicencio",
    "47001": "Tunja",
    "41001": "Neiva",
    "23001": "Montería",
    "20001": "Valledupar",
    "19001": "Popayán",
    "17001": "Manizales",
    "13001": "Cartagena",
    "8001": "Barranquilla",
    "66001": "Pereira",
    "63001": "Armenia",
    "88001": "San Andrés",
    "94001": "Inírida",
    "95001": "San José del Guaviare",
    "97001": "Mitú",
    "99001": "Puerto Carreño"
}

def process_covid_data(df):
    """
    Procesa los datos crudos de COVID-19 para presentación
    
    Args:
        df (pandas.DataFrame): DataFrame con datos crudos
    
    Returns:
        pandas.DataFrame: DataFrame procesado con columnas seleccionadas
    """
    if df is None or df.empty:
        return None
    
    # Crear una copia para no modificar el original
    processed_df = df.copy()
    
    # Mapeo de columnas disponibles en el dataset
    column_options = {
        'ciudad_municipio_nom': 'Ciudad de Ubicación',
        'ciudad_de_ubicación': 'Ciudad de Ubicación',
        'departamento_nom': 'Departamento', 
        'edad': 'Edad',
        'sexo': 'Sexo',
        'estado': 'Estado',
        'pais_procedencia': 'País de Procedencia',
        'fecha_reporte_web': 'Fecha Reporte',
        'id_de_caso': 'ID Caso'
    }
    
    # Encontrar qué columnas están disponibles en el dataset
    available_columns = {}
    for api_col, display_name in column_options.items():
        if api_col in processed_df.columns:
            available_columns[api_col] = display_name
    
    # Seleccionar solo las columnas disponibles
    processed_df = processed_df[list(available_columns.keys())]
    
    # Renombrar columnas
    processed_df = processed_df.rename(columns=available_columns)
    
    # Convertir códigos DANE a nombres de ciudad si es necesario
    if 'Ciudad de Ubicación' in processed_df.columns:
        processed_df['Ciudad de Ubicación'] = processed_df['Ciudad de Ubicación'].apply(
            lambda x: CODIGOS_DANE.get(str(x), str(x))
        )
    
    # Ordenar columnas para mejor presentación
    preferred_order = [
        'ID Caso', 'Fecha Reporte', 'Ciudad de Ubicación', 'Departamento', 
        'Edad', 'Sexo', 'Estado', 'País de Procedencia'
    ]
    
    # Mantener solo las columnas que existen en el orden preferido
    final_columns = [col for col in preferred_order if col in processed_df.columns]
    processed_df = processed_df[final_columns]
    
    return processed_df