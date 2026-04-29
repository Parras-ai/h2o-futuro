import streamlit as st
import time
import random
import pandas as pd

# 1. CONFIGURACIÓN
st.set_page_config(
    page_title="H2O - Central Hidroeléctrica",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ESTILOS CSS (Toque Futurista LED)
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; font-family: 'Courier New', monospace; }
    h1 { color: #00ffcc; text-shadow: 0 0 15px #00ffcc; text-align: center; }
    h2, h3 { color: #ff00ff; text-shadow: 0 0 10px #ff00ff; }
    .stMetric { background-color: #111111; border: 2px solid #00ffcc; border-radius: 15px; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. TÍTULO
st.title("⚡ SISTEMA CENTRAL HIDROELÉCTRICA H2O")
st.markdown("<h3 style='text-align: center; color: #ffffff;'>Colegio Bética-Mudarra</h3>", unsafe_allow_html=True)
st.markdown("---")

# 4. PESTAÑAS
tab_inicio, tab_ingenieria, tab_live = st.tabs(["🚀 VISIÓN GENERAL", "⚙️ ESQUEMA TÉCNICO", "📊 MONITORIZACIÓN LIVE"])

with tab_inicio:
    st.header("Visión Global")
    st.write("Prototipo avanzado de gestión energética inspirado en el Tajo de la Encantada.")
    st.info("💡 Concepto: Almacenamiento por Bombeo y Recuperación SREC.")

with tab_ingenieria:
    st.header("Análisis de Componentes")
    with st.expander("💧 Embalses y Sensores Infrarrojos"):
        st.write("Control de energía potencial y monitoreo de niveles en tiempo real.")
    with st.expander("🌀 Tecnología SREC y Turbinas"):
        st.write("Sistema de recuperación de energía para maximizar el rendimiento.")

with tab_live:
    st.header("Panel de Control en Tiempo Real")
    
    # SOLUCIÓN ERROR 3: Creamos el contenedor vacío
    metric_placeholder = st.empty()
    
    # SOLUCIÓN ERROR 4: Tabla profesional con Dataframe
    st.subheader("Estado de Componentes")
    df_estado = pd.DataFrame({
        "Componente": ["Turbina 1", "Turbina 2", "Bomba SREC", "Sensor Nivel"],
        "Estado": ["OPERATIVO", "OPERATIVO", "STANDBY", "ACTIVO"],
        "Carga": ["100%", "100%", "0%", "N/A"]
    })
    st.dataframe(df_estado, use_container_width=True)

# 5. BARRA LATERAL (Sidebar)
st.sidebar.title("Información")
st.sidebar.write("**Autor:** Parras")
st.sidebar.write("**Centro:** Colegio Bética-Mudarra")
st.sidebar.markdown("---")

# SOLUCIÓN ERROR 1: URL del QR corregida (sin saltos de línea)
url_app = "https://h2o-futuro.streamlit.app"
qr_api = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={url_app}"
st.sidebar.image(qr_api, caption="Escanea para acceder")

# SOLUCIÓN ERROR 2: Bucle para que los datos sean REALMENTE Live
# Este bucle actualiza las métricas cada 2 segundos sin recargar el resto de la pestaña
while True:
    with metric_placeholder.container():
        c1, c2, c3 = st.columns(3)
        # Generamos valores que oscilan ligeramente
        p = random.uniform(358.5, 362.2)
        n = random.uniform(84.1, 85.9)
        e = random.uniform(98.2, 99.1)
        
        c1.metric("POTENCIA", f"{p:.2f} MW", f"{random.uniform(-0.5, 0.5):.2f}")
        c2.metric("NIVEL AGUA", f"{n:.1f} %")
        c3.metric("EFICIENCIA", f"{e:.2f} %")
    
    time.sleep(2) # Pausa de 2 segundos antes de la siguiente actualización
