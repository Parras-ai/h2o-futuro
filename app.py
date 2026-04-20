import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="H2O - Central Hidroeléctrica",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ESTILOS CSS: Diseño Futurista LED
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        color: #00ffcc;
        font-family: 'Courier New', monospace;
    }
    h1 {
        color: #00ffcc;
        text-shadow: 0 0 15px #00ffcc;
        text-align: center;
        padding-bottom: 20px;
    }
    h2, h3 {
        color: #ff00ff;
        text-shadow: 0 0 10px #ff00ff;
        padding-top: 20px;
    }
    .stMetric {
        background-color: #111111;
        border: 2px solid #00ffcc;
        border-radius: 15px;
        padding: 20px;
    }
    .stInfo {
        background-color: rgba(0, 255, 255, 0.1);
        color: #ffffff;
        border-left: 5px solid #00ffcc;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. TÍTULO PRINCIPAL
st.title("⚡ SISTEMA CENTRAL HIDROELÉCTRICA H2O")
st.markdown("<h3 style='text-align: center; color: #ffffff;'>Innovación Sostenible Inspirada en el Tajo de la Encantada</h3>", unsafe_allow_html=True)
st.markdown("---")

# 4. ESTRUCTURA DE PESTAÑAS
tab_inicio, tab_ingenieria, tab_live = st.tabs(["🚀 VISIÓN GENERAL", "⚙️ ESQUEMA TÉCNICO", "📊 MONITORIZACIÓN"])

# --- PESTAÑA 1: INICIO ---
with tab_inicio:
    st.header("Visión Global del Proyecto")
    st.write("""
    Esta central representa la **H2O-Futuro**, un prototipo avanzado de gestión energética.
    Inspirada en la central de bombeo del Tajo de la Encantada (Málaga), nuestro diseño
    integra tecnologías limpias para crear una **batería natural de alta eficiencia**.
    """)
    st.info("💡 **Concepto Clave:** Sistema Hidroeólico con Almacenamiento por Bombeo y Recuperación SREC.")
    st.success("🟢 ESTADO: Red Conectada")

# --- PESTAÑA 2: INGENIERÍA ---
with tab_ingenieria:
    st.header("Análisis de Componentes")
    
    with st.expander("💧 EMBALSES (Superior e Inferior)"):
        st.write("Dos embalses a distintas alturas. El superior almacena agua en horas de baja demanda y el inferior la recoge tras la generación, actuando como una batería de energía potencial.")

    with st.expander("🆔 SENSORES DE INFRARROJOS (Control de Nivel)"):
        st.write("Sensores de precisión para monitorear el nivel de agua en tiempo real, previniendo desbordamientos y optimizando los ciclos de bombeo.")

    with st.expander("🚇 TUBERÍA TRANSPARENTE (Conducción Hidráulica)"):
        st.write("Tuberías de alta presión y transparencia para inspección visual y didáctica, garantizando un transporte con mínima pérdida por fricción.")

    with st.expander("🌀 TURBINAS Y RECUPERADOR (SREC)"):
        st.write("Sistema de alta eficiencia que genera electricidad en horas punta y permite el bombeo de agua mediante la recuperación de energía excedente (SREC).")

    with st.expander("📱 APP DE CONTROL (Interfaz Digital)"):
        st.write("Centro de mando digital para el monitoreo de todos los parámetros: potencia, nivel de agua y estado de turbinas.")

# --- PESTAÑA 3: MONITORIZACIÓN ---
with tab_live:
    st.header("Panel de Control Energético")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("POTENCIA ACTUAL", "1.2 GW", "12%")
    col2.metric("NIVEL EMBALSE", "85%", "Estable")
    col3.metric("EFICIENCIA SREC", "98.5%", "Alta")

    st.subheader("Estado de Componentes")
    st.table({
        "Componente": ["Turbina 1", "Turbina 2", "Bomba 1", "Sensor Nivel", "Tubería"],
        "Estado": ["OPERATIVA", "OPERATIVA", "STANDBY", "OPERATIVO", "ÓPTIMO"],
        "Carga": ["100%", "100%", "0%", "N/A", "100%"]
    })

# 5. BARRA LATERAL
st.sidebar.title("Información")
st.sidebar.write("**Autor:** Parras")
st.sidebar.write("**Centro:** Colegio Bética-Mudarra")
st.sidebar.markdown("---")

st.sidebar.subheader("📱 Escanea para acceder")
# Sustituye la URL al final por la dirección real de tu app publicada
st.sidebar.image("https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://h2o-futuro.streamlit.app")
st.sidebar.write("Acceso a la documentación oficial.")
