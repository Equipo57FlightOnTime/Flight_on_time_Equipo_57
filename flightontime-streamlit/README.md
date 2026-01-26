# FlightOnTime - Streamlit App

Aplicación web interactiva con Streamlit para consultar predicciones de retrasos de vuelos.

## 🎨 Características

✅ **Interfaz moderna e intuitiva** con Streamlit  
✅ **Diseño responsivo** y profesional  
✅ **Carga automática de CSVs** (aeropuertos y aerolíneas)  
✅ **Gráficos interactivos** con Plotly  
✅ **Indicador tipo gauge** para probabilidad de retraso  
✅ **Validaciones en tiempo real**  
✅ **Estado del servidor** en sidebar  
✅ **Métricas visuales** de los datos  
✅ **Manejo de errores** robusto  

## 📁 Estructura de Archivos

```
flightontime-streamlit/
├── app.py                  # Aplicación principal de Streamlit
├── requirements.txt        # Dependencias de Python
├── aeropuertos.csv        # Datos de aeropuertos
├── aerolineas.csv         # Datos de aerolíneas
└── README.md              # Este archivo
```

## 🚀 Instalación y Ejecución

### Paso 1: Instalar dependencias

```bash
# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 2: Ejecutar la aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en: `http://localhost:8501`

## 📊 Características Detalladas

### 1. **Sidebar Inteligente**
- 🟢 **Monitoreo en tiempo real** del estado de Spring Boot y FastAPI
- 📊 **Estadísticas** de aeropuertos y aerolíneas cargadas
- ℹ️ **Información** del modelo y precisión

### 2. **Formulario Interactivo**
- 📅 Selector de fecha con calendario
- 🕐 Selector de hora visual
- 🛫 Selectores filtrados de aeropuertos
- ✈️ Selector de aerolíneas

### 3. **Visualización de Resultados**
- 🎯 **Gauge circular** con la probabilidad de retraso
- ✅/⏰ **Alertas visuales** según el resultado
- 📋 **Métricas detalladas** del vuelo
- 🎨 **Colores dinámicos** según la probabilidad

### 4. **Gráfico de Probabilidad**
- 🟢 Verde (0-30%): Baja probabilidad de retraso
- 🟡 Amarillo (30-70%): Probabilidad media
- 🔴 Rojo (70-100%): Alta probabilidad de retraso


## 📋 Formato de los CSV

### aeropuertos.csv

```csv
LAT,LON,IATA,AIRPORT_NAME
-23.432616,-46.469444,GRU,Aeroporto Internacional de São Paulo/Guarulhos
-22.809999,-43.250557,GIG,Aeroporto Internacional do Rio de Janeiro/Galeão
```

**Columnas requeridas:**
- `IATA`: Código IATA (3 letras)
- `AIRPORT_NAME`: Nombre del aeropuerto
- `LAT`, `LON`: Opcional (para futuras features)

### aerolineas.csv

```csv
AIRLINE_NAME,AIRLINE_IATA
LATAM Airlines,LA
Gol Linhas Aéreas,G3
```

**Columnas requeridas:**
- `AIRLINE_IATA`: Código IATA (2 letras)
- `AIRLINE_NAME`: Nombre de la aerolínea

## 🔌 Requisitos del Backend

### Spring Boot (Puerto 8080)

**Endpoint:** `POST /predict`

**Request:**
```json
{
  "aerolinea": "LA",
  "origen": "GIG",
  "destino": "GRU",
  "hora_partida": 14,
  "dia_semana": 3
}
```

**Response:**
```json
{
  "prevision": "PUNTUAL",
  "probabilidad": 0.23
}
```

## 🎯 Flujo de Trabajo

1. Usuario abre la app en el navegador
2. Streamlit carga los CSVs automáticamente
3. Los selectores se pueblan con los datos
4. Usuario completa el formulario
5. Click en "CONSULTAR PREDICCIÓN"
6. La app valida los datos
7. Hace POST request a Spring Boot
8. Muestra resultado con animación y gráficos
9. Sidebar actualiza estado de conexión


## 🐛 Solución de Problemas

### Error: "No se pudo conectar con el servidor"

**Causa:** Spring Boot no está corriendo

**Solución:**
```bash
cd C:\git\hackathon-flighontime
mvn spring-boot:run
```

### Error: "No se encontró el archivo CSV"

**Causa:** Los CSVs no están en la misma carpeta que `app.py`

**Solución:**
- Asegúrate que `aeropuertos.csv` y `aerolineas.csv` estén en la misma carpeta
- O cambia la ruta en el código

### La app se ve rara

**Causa:** Versión desactualizada de Streamlit

**Solución:**
```bash
pip install --upgrade streamlit
```

### Los gráficos no se muestran

**Causa:** Falta Plotly

**Solución:**
```bash
pip install plotly
```

## 📱 Modo Responsive

Streamlit es automáticamente responsive y funciona en:
- 💻 Desktop
- 📱 Tablets  
- 📱 Móviles

## 🔗 Recursos Adicionales

- [Documentación de Streamlit](https://docs.streamlit.io)
- [Galería de Streamlit](https://streamlit.io/gallery)
- [Plotly Charts](https://plotly.com/python/)
- [Componentes de Streamlit](https://streamlit.io/components)


## 📄 Licencia

Proyecto académico para el Hackathon FlightOnTime.

---

