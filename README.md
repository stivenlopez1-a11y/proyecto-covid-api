 🦠 COVID-19 Data API - Colombia

Sistema de consulta de datos de casos COVID-19 en Colombia mediante la API del Portal Nacional de Datos Abiertos. Desarrollado en Python con arquitectura modular.

## 🏗️ Arquitectura del Proyecto
proyecto-covid-api/
├── main.py # Punto de entrada principal
├── api/
│ ├── init.py # Inicializador del módulo API
│ └── covid_api.py # Cliente para API de Datos Abiertos
├── ui/
│ ├── init.py # Inicializador del módulo UI
│ └── user_interface.py # Interfaz de usuario por consola
├── utils/
│ ├── init.py # Inicializador del módulo Utils
│ └── data_utils.py # Utilidades de procesamiento de datos
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación

text

## 🚀 Características

- ✅ Consulta de casos COVID-19 por departamento
- ✅ Límite personalizable de registros
- ✅ Procesamiento y transformación de datos
- ✅ Conversión de códigos DANE a nombres de ciudades
- ✅ Interfaz de usuario intuitiva por consola
- ✅ Arquitectura modular escalable

## 📦 Instalación

### Prerrequisitos
- Python 3.8+
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clonar el repositorio**:
```bash
git clone https://github.com/stivenlopez1-a11y/proyecto-covid-api.git
cd proyecto-covid-api
Crear entorno virtual:

bash
python -m venv venv
Activar entorno virtual:

bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
Instalar dependencias:

bash
pip install -r requirements.txt
🎯 Uso
Ejecutar la aplicación:

bash
python main.py
Seguir las instrucciones:

Ingresar el nombre del departamento

Especificar el límite de registros

Ver resultados en formato tabular con las columnas:

Ciudad de ubicación

Departamento

Edad

Sexo

Estado

País de procedencia

🔗 Fuente de Datos
Los datos se obtienen del Portal de Datos Abiertos de Colombia mediante el dataset:

Dataset: Casos positivos de COVID-19 en Colombia

ID: gt2j-8ykr

API: API Socrata

🛠️ Tecnologías Utilizadas
Python 3.13 - Lenguaje de programación

Pandas - Procesamiento y análisis de datos

Sodapy - Cliente para APIs Socrata

API Socrata - Estándar para datos abiertos gubernamentales

📊 Módulos del Sistema
🔌 Módulo API (api/covid_api.py)
Conexión con API de Datos Abiertos

Consultas parametrizadas por departamento

Manejo de errores y timeouts

👤 Módulo UI (ui/user_interface.py)
Interfaz de usuario por consola

Validación de entradas de usuario

Presentación formateada de resultados

⚙️ Módulo Utils (utils/data_utils.py)
Procesamiento y transformación de datos

Conversión de códigos DANE a nombres de ciudades

Selección y renombrado de columnas

🎨 Ejemplo de Uso
text
=== CONSULTA DE DATOS COVID-19 EN COLOMBIA ===
Fuente: Portal Nacional de Datos Abiertos

Por favor ingrese los siguientes datos para la consulta:
--------------------------------------------------
Departamento: Risaralda
Límite de registros (máximo 1000 recomendado): 10

Consultando datos para Risaralda...
Conectando con la API de Datos Abiertos...
Datos obtenidos: 10 registros

========================================================================================================================
RESULTADOS DE LA CONSULTA - CASOS COVID-19
========================================================================================================================
 ID Caso       Fecha Reporte    Ciudad de Ubicación Departamento    Edad Sexo Estado   País de Procedencia
1137442  2020-11-08T00:00:00.000            Pereira    RISARALDA       81    M  Leve                 Colombia
1137444  2020-11-08T00:00:00.000            Pereira    RISARALDA       64    F  Leve                 Colombia
========================================================================================================================
📝 Próximas Mejoras
Implementar interfaz gráfica (GUI)

Agregar filtros adicionales (edad, sexo, estado)

Generar reportes en PDF/Excel

Implementar caché de consultas

Agregar visualizaciones gráficas

👨‍💻 Autor
Stiven Lopez

GitHub: @stivenlopez1-a11y

Proyecto académico para Universidad Tecnológica de Pereira

📄 Licencia
Este proyecto es con fines educativos. Los datos pertenecen al Portal de Datos Abiertos de Colombia.

¡Contribuciones y sugerencias son bienvenidas! 🚀