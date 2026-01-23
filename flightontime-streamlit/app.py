import streamlit as st
import pandas as pd
import requests
from datetime import datetime, time
import plotly.graph_objects as go
import plotly.express as px

# ==================== CONFIGURACIÓN DE LA PÁGINA ====================
st.set_page_config(
    page_title="FlightOnTime - Predicción Inteligente",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== ESTILOS PERSONALIZADOS ====================
st.markdown("""
<style>
    /* Main container */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Headers */
    h1 {
        color: #1e3a8a;
        text-align: center;
        font-size: 3rem !important;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Cards */
    .stCard {
        background: white;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Success/Error messages */
    .success-box {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        margin: 2rem 0;
    }
    
    .error-box {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        margin: 2rem 0;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: bold;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 0.5rem;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(6, 182, 212, 0.4);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #334155 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# ==================== CONFIGURACIÓN DE LA API ====================
API_URL = "http://localhost:8080/predict"

# ==================== FUNCIONES DE CARGA DE DATOS ====================
@st.cache_data
def load_aeropuertos():
    """Carga los aeropuertos desde el archivo CSV"""
    try:
        df = pd.read_csv('aeropuertos.csv')
        # Limpiar datos
        df = df.dropna(subset=['IATA', 'AIRPORT_NAME'])
        # AGREGAR ESTAS LÍNEAS:
        df['IATA'] = df['IATA'].str.strip()
        df['AIRPORT_NAME'] = df['AIRPORT_NAME'].str.strip()
        df = df.sort_values('AIRPORT_NAME')
        return df
    except FileNotFoundError:
        st.error("⚠️ No se encontró el archivo 'aeropuertos.csv'")
        # Datos de ejemplo si falla
        return pd.DataFrame({
            'IATA': ['GIG', 'GRU', 'BSB', 'CGH'],
            'AIRPORT_NAME': [
                'Aeroporto Internacional do Rio de Janeiro/Galeão',
                'Aeroporto Internacional de São Paulo/Guarulhos',
                'Aeroporto Internacional de Brasília',
                'Aeroporto de São Paulo/Congonhas'
            ]
        })

@st.cache_data
def load_aerolineas():
    """Carga las aerolíneas desde el archivo CSV"""
    try:
        df = pd.read_csv('aerolineas.csv')
        # Limpiar datos
        df = df.dropna(subset=['AIRLINE_IATA', 'AIRLINE_NAME'])
        # AGREGAR ESTA LÍNEA PARA LIMPIAR ESPACIOS:
        df['AIRLINE_IATA'] = df['AIRLINE_IATA'].str.strip()
        df['AIRLINE_NAME'] = df['AIRLINE_NAME'].str.strip()
        df = df.sort_values('AIRLINE_NAME')
        return df
    except FileNotFoundError:
        st.error("⚠️ No se encontró el archivo 'aerolineas.csv'")
        # Datos de ejemplo si falla
        return pd.DataFrame({
            'AIRLINE_IATA': ['LA', 'G3', 'AD', 'AA'],
            'AIRLINE_NAME': [
                'LATAM Airlines',
                'Gol Linhas Aéreas',
                'Azul Brazilian Airlines',
                'American Airlines'
            ]
        })

# ==================== FUNCIÓN DE PREDICCIÓN ====================
def get_prediction(aerolinea, origen, destino, hora_partida, dia_semana):
    """Envía la petición a la API y retorna la predicción"""
    
    payload = {
        "aerolinea": aerolinea,
        "origen": origen,
        "destino": destino,
        "hora_partida": hora_partida,
        "dia_semana": dia_semana
    }
    
    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        response.raise_for_status()
        return response.json(), None
    except requests.exceptions.ConnectionError:
        return None, "❌ No se pudo conectar con el servidor. Verifica que Spring Boot esté corriendo en el puerto 8080."
    except requests.exceptions.Timeout:
        return None, "⏱️ La petición tardó demasiado. Intenta de nuevo."
    except requests.exceptions.HTTPError as e:
        return None, f"❌ Error HTTP: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return None, f"❌ Error inesperado: {str(e)}"

# ==================== FUNCIÓN PARA CREAR GRÁFICO ====================
def create_probability_gauge(probability):
    """Crea un gráfico de tipo gauge para mostrar la probabilidad"""
    
    # Convertir probabilidad a porcentaje
    probability_percent = probability * 100
    
    # Determinar color basado en la probabilidad
    if probability_percent < 30:
        color = "#10b981"  # Verde
    elif probability_percent < 70:
        color = "#f59e0b"  # Amarillo
    else:
        color = "#ef4444"  # Rojo
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = probability_percent,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Probabilidad de Retraso", 'font': {'size': 24}},
        number = {'suffix': "%", 'font': {'size': 48}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': color},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': '#d1fae5'},
                {'range': [30, 70], 'color': '#fef3c7'},
                {'range': [70, 100], 'color': '#fee2e2'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor = "rgba(0,0,0,0)",
        plot_bgcolor = "rgba(0,0,0,0)",
        font = {'color': "#1e293b", 'family': "Arial"},
        height = 300
    )
    
    return fig

# ==================== CARGAR DATOS ====================
df_aeropuertos = load_aeropuertos()
df_aerolineas = load_aerolineas()

# ==================== SIDEBAR ====================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/airplane-take-off.png", width=100)
    st.title("⚙️ Configuración")
    
    st.markdown("---")
    
    # Información de la API
    st.subheader("📡 Estado del Servicio")
    
    # Verificar Spring Boot
    spring_boot_status = False
    # Verificar Spring Boot
    spring_boot_status = False
    try:
        response = requests.get("http://localhost:8080/", timeout=2)
        spring_boot_status = True  # Si llega aquí, está corriendo (incluso con error 404)
    except:
        pass
    
    if spring_boot_status:
        st.success("✅ Spring Boot: Conectado")
    else:
        st.error("❌ Spring Boot: Desconectado")
    
    # Verificar FastAPI
    fastapi_status = False
    try:
        response = requests.get("http://127.0.0.1:8000/", timeout=2)
        fastapi_status = True  # Si llega aquí, está corriendo
    except:
        pass
    
    if fastapi_status:
        st.success("✅ FastAPI: Conectado")
    else:
        st.error("❌ FastAPI: Desconectado")
    
    st.markdown("---")
    
    # Estadísticas
    st.subheader("📊 Estadísticas")
    st.metric("Aeropuertos disponibles", len(df_aeropuertos))
    st.metric("Aerolíneas disponibles", len(df_aerolineas))
    
    st.markdown("---")
    
    # Información adicional
    st.subheader("ℹ️ Información")
    st.info("""
    **FlightOnTime** utiliza Machine Learning para predecir retrasos en vuelos.
    
    **Precisión del modelo:** 98%
    
    **Datos procesados:** +10M registros
    """)

# ==================== MAIN CONTENT ====================
# Header
st.title("✈️ Predicción Inteligente FlightOnTime")
st.markdown('<p class="subtitle">Optimiza tu viaje con análisis de datos avanzado y machine learning de última generación.</p>', 
            unsafe_allow_html=True)

# Separador
st.markdown("---")

# Formulario
st.subheader("🔍 Consultar Vuelo")
st.write("Ingresa los detalles de tu vuelo para obtener una predicción precisa")

col1, col2 = st.columns(2)

with col1:
    # Fecha del vuelo
    fecha_vuelo = st.date_input(
        "📅 Fecha del vuelo",
        value=datetime.today(),
        help="Selecciona la fecha de tu vuelo"
    )
    
    # Aeropuerto de origen
    aeropuertos_origen = df_aeropuertos['IATA'].tolist()
    nombres_origen = [f"{row['IATA']} - {row['AIRPORT_NAME']}" for _, row in df_aeropuertos.iterrows()]
    
    origen_selected = st.selectbox(
        "🛫 Aeropuerto de Origen",
        options=range(len(nombres_origen)),
        format_func=lambda x: nombres_origen[x],
        help="Selecciona el aeropuerto de salida"
    )
    origen_iata = aeropuertos_origen[origen_selected]
    
    # Aerolínea
    aerolineas_iata = df_aerolineas['AIRLINE_IATA'].tolist()
    nombres_aerolineas = [f"{row['AIRLINE_IATA']} - {row['AIRLINE_NAME']}" for _, row in df_aerolineas.iterrows()]
    
    aerolinea_selected = st.selectbox(
        "✈️ Aerolínea",
        options=range(len(nombres_aerolineas)),
        format_func=lambda x: nombres_aerolineas[x],
        help="Selecciona la compañía aérea"
    )
    aerolinea_iata = aerolineas_iata[aerolinea_selected]

with col2:
    # Hora de salida
    hora_salida = st.time_input(
        "🕐 Hora de salida",
        value=time(14, 0),
        help="Selecciona la hora de salida del vuelo"
    )
    
    # Aeropuerto de destino
    aeropuertos_destino = df_aeropuertos['IATA'].tolist()
    nombres_destino = [f"{row['IATA']} - {row['AIRPORT_NAME']}" for _, row in df_aeropuertos.iterrows()]
    
    destino_selected = st.selectbox(
        "🛬 Aeropuerto de Destino",
        options=range(len(nombres_destino)),
        format_func=lambda x: nombres_destino[x],
        help="Selecciona el aeropuerto de llegada"
    )
    destino_iata = aeropuertos_destino[destino_selected]

# Espacio
st.markdown("<br>", unsafe_allow_html=True)

# Botón de predicción
predict_button = st.button("🚀 CONSULTAR PREDICCIÓN", use_container_width=True)

# ==================== PROCESAMIENTO Y RESULTADO ====================
if predict_button:
    # Validaciones
    if origen_iata == destino_iata:
        st.error("⚠️ El aeropuerto de origen y destino deben ser diferentes")
    else:
        # Calcular día de la semana (0 = Lunes, 6 = Domingo)
        dia_semana = fecha_vuelo.weekday()
        
        # Extraer hora
        hora_partida = hora_salida.hour
        
        # Mostrar spinner mientras se hace la petición
        with st.spinner('🔄 Analizando datos del vuelo...'):
            # Hacer la predicción
            result, error = get_prediction(
                aerolinea_iata, 
                origen_iata, 
                destino_iata, 
                hora_partida, 
                dia_semana
            )
        
        if error:
            st.error(error)
        elif result:
            # Separador
            st.markdown("---")
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Determinar si es puntual o retrasado
            is_puntual = result.get('prevision') in ['PUNTUAL', 'Puntual']
            probabilidad = result.get('probabilidad', 0)
            
            # Título del resultado
            if is_puntual:
                st.markdown("""
                <div class="success-box">
                    <h2>✅ ¡Buenas noticias!</h2>
                    <h1>VUELO PUNTUAL</h1>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="error-box">
                    <h2>⏰ Atención</h2>
                    <h1>POSIBLE RETRASO</h1>
                </div>
                """, unsafe_allow_html=True)
            
            # Mostrar gráfico de probabilidad
            st.plotly_chart(create_probability_gauge(probabilidad), use_container_width=True)
            
            # Detalles del vuelo
            st.subheader("📋 Detalles del Vuelo")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("🛫 Origen", f"{origen_iata}")
                origen_nombre = df_aeropuertos[df_aeropuertos['IATA'] == origen_iata]['AIRPORT_NAME'].values[0]
                st.caption(origen_nombre)
                
            with col2:
                st.metric("🛬 Destino", f"{destino_iata}")
                destino_nombre = df_aeropuertos[df_aeropuertos['IATA'] == destino_iata]['AIRPORT_NAME'].values[0]
                st.caption(destino_nombre)
                
            with col3:
                st.metric("✈️ Aerolínea", f"{aerolinea_iata}")
                aerolinea_nombre = df_aerolineas[df_aerolineas['AIRLINE_IATA'] == aerolinea_iata]['AIRLINE_NAME'].values[0]
                st.caption(aerolinea_nombre)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            col4, col5, col6 = st.columns(3)
            
            dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
            
            with col4:
                st.metric("📅 Fecha", fecha_vuelo.strftime("%d/%m/%Y"))
                st.caption(dias_semana[dia_semana])
                
            with col5:
                st.metric("🕐 Hora", hora_salida.strftime("%H:%M"))
                st.caption(f"Hora de partida: {hora_partida}:00")
                
            with col6:
                st.metric("📊 Probabilidad", f"{(probabilidad * 100):.1f}%")
                st.caption("de retraso")

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 2rem 0;">
    <p>© 2024 FlightOnTime. Tecnología de vanguardia para tu tranquilidad.</p>
    <p>
        <a href="#" style="color: #06b6d4; margin: 0 1rem;">Privacidad</a>
        <a href="#" style="color: #06b6d4; margin: 0 1rem;">Términos</a>
        <a href="#" style="color: #06b6d4; margin: 0 1rem;">Soporte</a>
    </p>
</div>
""", unsafe_allow_html=True)
