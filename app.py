import streamlit as st
import time
import random
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
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
    h2, h3 { color: #ff00ff; text-shadow: 0 0 10px #ff00ff; padding-top: 20px; }
    .stMetric { background-color: #111111; border: 2px solid #00ffcc; border-radius: 15px; padding: 20px; }
    .stInfo { background-color: rgba(0, 255, 255, 0.1); color: #ffffff; border-left: 5px solid #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# 3. TÍTULO Y CABECERA
st.title("⚡ SISTEMA CENTRAL HIDROELÉCTRICA H2O")
st.markdown("<h3 style='text-align: center; color: #ffffff;'>Colegio Bética-Mudarra</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00ffcc;'>Innovación Sostenible Inspirada en el Tajo de la Encantada</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. PESTAÑAS PRINCIPALES
tab_inicio, tab_ingenieria, tab_live = st.tabs(["🚀 VISIÓN GENERAL", "⚙️ ESQUEMA TÉCNICO", "📊 MONITORIZACIÓN LIVE"])

# --- PESTAÑA 1: VISIÓN GENERAL ---
with tab_inicio:
    st.header("Visión Global del Proyecto")
    st.write("""
    Esta central representa la **H2O-Futuro**, un prototipo avanzado de gestión energética.
    Inspirada en la central de bombeo del Tajo de la Encantada (Málaga), nuestro diseño
    integra tecnologías limpias para crear una **batería natural de alta eficiencia**.
    """)
    st.info("💡 **Concepto Clave:** Sistema Hidroeólico con Almacenamiento por Bombeo y Recuperación SREC.")
    st.success("🟢 ESTADO DEL SISTEMA: Conectado a la Red")

# --- PESTAÑA 2: ESQUEMA TÉCNICO (TODOS LOS DATOS RECUPERADOS) ---
with tab_ingenieria:
    st.header("Análisis Detallado de Componentes")
    st.write("Explora cada elemento técnico que compone el sistema H2O.")

    with st.expander("💧 EMBALSES (Superior e Inferior)"):
        st.write("""
        **Estructura de Almacenamiento:**
        - **Embalse Superior (H2O-UP):** Almacena agua en horas de baja demanda eléctrica.
        - **Embalse Inferior (H2O-DOWN):** Recoge el agua tras el proceso de generación.
        **Función:** Actúan como una batería de energía potencial mediante gravedad.
        """)

    with st.expander("🆔 SENSORES DE INFRARROJOS (Control de Nivel)"):
        st.write("""
        **Tecnología de Precisión:**
        - Sensores de infrarrojos encargados de monitorear el nivel de agua en tiempo real.
        - **Optimización:** Previenen desbordamientos y calculan el momento exacto para iniciar el ciclo de bombeo.
        """)

    with st.expander("🚇 TUBERÍA TRANSPARENTE (Conducción Hidráulica)"):
        st.write("""
        **Diseño Industrial:**
        - Tuberías de alta presión fabricadas con materiales transparentes para inspección visual.
        - **Eficiencia:** Diseñadas para un transporte de flujo constante con mínima pérdida por fricción.
        """)

    with st.expander("🌀 TURBINAS Y RECUPERADOR (Tecnología SREC)"):
        st.write("""
        **El Corazón de la Central:**
        - **Turbinas:** Generación de electricidad de alto rendimiento.
        - **SREC (Sistema de Recuperación de Energía):** Tecnología innovadora que recupera los excedentes de energía para maximizar la eficiencia global del sistema durante el bombeo.
        """)

    with st.expander("📱 APP DE CONTROL (Interfaz Digital)"):
        st.write("""
        **Centro de Mando:** Interfaz digital para el monitoreo de todos los parámetros operativos: potencia, niveles, estado de válvulas y eficiencia SREC.
        """)

# --- PESTAÑA 3: MONITORIZACIÓN LIVE ---
with tab_live:
    st.header("Panel de Control Energético")
    
    # Contenedor para las métricas que cambiarán
    metric_placeholder = st.empty()
    
    st.subheader("Estado de Componentes del Sistema")
    df_estado = pd.DataFrame({
        "Componente": ["Turbina Principal", "Generador SREC", "Bomba 1", "Sensores IR", "Tubería Principal"],
        "Estado": ["OPERATIVO", "OPERATIVO", "STANDBY", "ACTIVO", "FLUJO ÓPTIMO"],
        "Rendimiento": ["98%", "99%", "0%", "100%", "100%"]
    })
    st.dataframe(df_estado, use_container_width=True)

# 5. BARRA LATERAL (Sidebar)
st.sidebar.title("Información")
st.sidebar.write("**Autor:** Parras")
st.sidebar.write("**Centro:** Colegio Bética-Mudarra")
st.sidebar.markdown("---")

# QR Corregido
url_app = "https://h2o-futuro.streamlit.app"
qr_api = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={url_app}"
st.sidebar.subheader("📱 Acceso Móvil")
st.sidebar.image(qr_api, caption="Escanea para acceder")

# 6. BUCLE DE ACTUALIZACIÓN LIVE (Solo para las métricas)
while True:
    with metric_placeholder.container():
        c1, c2, c3 = st.columns(3)
        # Datos simulados que oscilan
        potencia = random.uniform(359.2, 361.8)
        nivel = random.uniform(84.5, 85.5)
        eficiencia = random.uniform(98.4, 99.1)
        
        c1.metric("POTENCIA GENERADA", f"{potencia:.2f} MW", f"{random.uniform(-0.4, 0.4):.2f}")
        c2.metric("NIVEL AGUA", f"{nivel:.1f} %")
        c3.metric("EFICIENCIA SREC", f"{eficiencia:.2f} %")
    
    time.sleep(2)
