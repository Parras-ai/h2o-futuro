import streamlit as st

# Configuración de página
st.set_page_config(page_title="H2O - Central Futurista", layout="wide")

# CSS para el toque FUTURISTA Y LED
st.markdown("""
    <style>
    /* Fondo oscuro estilo terminal */
    .stApp { background-color: #050505; color: #00ffcc; font-family: 'Courier New', monospace; }
    
    /* Títulos con brillo LED */
    h1 { color: #00ffcc; text-shadow: 0 0 10px #00ffcc; text-align: center; }
    h2 { color: #ff00ff; text-shadow: 0 0 8px #ff00ff; }
    
    /* Tarjetas de datos tipo "Panel" */
    .stMetric { background-color: #111; border: 2px solid #00ffcc; border-radius: 15px; padding: 20px; box-shadow: 0 0 15px #00ffcc33; }
    
    /* Pestañas */
    button { color: #00ffcc !important; }
    </style>
    """, unsafe_allow_html=True)

# Título con estilo
st.title("⚡ SISTEMA CENTRAL H2O - MODO FUTURISTA")
st.markdown("---")

tab_inicio, tab_tecnico, tab_datos = st.tabs(["🚀 INICIO", "⚙️ ESQUEMA TÉCNICO", "🔋 PANEL DE CONTROL"])

with tab_inicio:
    st.header("BIENVENIDO AL CENTRO DE OPERACIONES")
    # Imagen de inicio (Nicho)
    st.image("Imagen1.png", caption="Visión general de la infraestructura H2O", use_container_width=True)
    st.write("Estado del Sistema: **ONLINE**")
    st.info("Central inspirada en la ingeniería del Tajo de la Encantada. Integración total de energías renovables y control digital.")

with tab_tecnico:
    st.header("ANÁLISIS DE COMPONENTES")
    # Imagen detallada
    st.image("Imagen2.png", caption="Esquema técnico detallado", use_container_width=True)
    
    # Columnas con iconos
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Infraestructura")
        st.write("🔹 Sensores Infrarrojos: Activos")
        st.write("🔹 Tubería Transparente: Flujo Óptimo")
    with col2:
        st.subheader("Tecnología SREC")
        st.write("🔹 Recuperación de energía: Máxima")
        st.write("🔹 Estabilidad de red: 99.9%")

with tab_datos:
    st.header("MONITOREO DE ENERGÍA")
    c1, c2, c3 = st.columns(3)
    c1.metric("POTENCIA", "360 MW", "12%")
    c2.metric("NIVEL EMBALSE", "85%", "Estable")
    c3.metric("EFICIENCIA", "98%", "Aumentando")
    
    st.table({
        "PARÁMETRO": ["Voltaje", "Estado Turbina", "Carga"],
        "VALOR": ["400kV", "OPERATIVA", "HIGH"]
    })

# Sidebar LED
st.sidebar.title("🚨 PANEL DE CONTROL")
st.sidebar.write("Acceso restringido - Autor: Parras")
if st.sidebar.button("EJECUTAR DIAGNÓSTICO"):
    st.sidebar.success("SISTEMA SIN ERRORES")
