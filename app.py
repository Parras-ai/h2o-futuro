import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="H2O - Central Hidroeléctrica",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo visual futurista/LED
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; font-family: 'Courier New', monospace; }
    h1 { color: #00ffcc; text-shadow: 0 0 10px #00ffcc; text-align: center; }
    h2, h3 { color: #ff00ff; text-shadow: 0 0 8px #ff00ff; }
    .stMetric { background-color: #111; border: 2px solid #00ffcc; border-radius: 10px; padding: 15px; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.title("⚡ SISTEMA CENTRAL H2O")
st.markdown("<h3 style='text-align: center; color: #ffffff;'>Innovación en el Tajo de la Encantada</h3>", unsafe_allow_html=True)
st.markdown("---")

# Pestañas principales
tab_vision, tab_tecnico, tab_datos = st.tabs(["🚀 VISIÓN GENERAL", "⚙️ ESQUEMA TÉCNICO", "📊 MONITORIZACIÓN"])

with tab_vision:
    st.header("Proyecto H2O-Futuro")
    st.write("Bienvenido al centro de gestión energética. Este proyecto investiga cómo transformar la energía hidráulica en un modelo de batería natural eficiente, sostenible e inteligente.")
    st.info("Inspirado en la tecnología de bombeo del Tajo de la Encantada, Málaga.")

with tab_tecnico:
    st.header("Componentes del Sistema")
    with st.expander("💧 Gestión de Embalses"):
        st.write("Sistema de doble embalse para almacenamiento de energía mediante diferencia de potencial.")
    with st.expander("🆔 Sensores de Infrarrojos"):
        st.write("Control de niveles y flujo en tiempo real para optimización de ciclos.")
    with st.expander("🚇 Conducción Hidráulica"):
        st.write("Red de tuberías de alta presión para la transferencia eficiente entre niveles.")
    with st.expander("🌀 Tecnología SREC"):
        st.write("Sistema de recuperación de energía excedente para maximizar el rendimiento global.")

with tab_datos:
    st.header("Datos de Producción en Tiempo Real")
    c1, c2, c3 = st.columns(3)
    c1.metric("POTENCIA", "360 MW")
    c2.metric("NIVEL AGUA", "85%")
    c3.metric("EFICIENCIA", "98.5%")

# Sidebar - Creditos y QR
st.sidebar.title("Información del Proyecto")
st.sidebar.write("**Autor:** Parras")
st.sidebar.write("**Centro:** Colegio Bética-Mudarra")
st.sidebar.markdown("---")

st.sidebar.subheader("📱 Escanea para acceder")
# Generador de QR automático (asegúrate de que la URL sea la de tu App)
st.sidebar.image("https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://h2o-futuro.streamlit.app") 
st.sidebar.write("Acceso a la documentación oficial.")
