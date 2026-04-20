import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Central H2O", layout="wide")

# Estilo para que se vea tecnológica
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: #e0e0e0; }
    h1, h2 { color: #00ffcc; }
    .stMetric { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.title("🌊 Central Hidroeléctrica H2O: Tajo de la Encantada")
st.markdown("---")

# Secciones de la App
tab1, tab2, tab3 = st.tabs(["🏠 Inicio", "⚙️ Funcionamiento", "📊 Datos Técnicos"])

with tab1:
    st.header("Bienvenido al Centro de Control")
    st.write("Este proyecto representa el funcionamiento de la central de bombeo del Tajo de la Encantada.")
    st.info("Utiliza las pestañas superiores para explorar los detalles técnicos y operativos del sistema.")

with tab2:
    st.header("¿Cómo funciona el bombeo?")
    st.write("""
    El sistema funciona como una **gran batería natural**:
    1. **Fase de Producción:** El agua cae desde el embalse superior, moviendo las turbinas para generar electricidad.
    2. **Fase de Bombeo:** En horas de poca demanda (y energía más barata), el sistema bombea el agua de vuelta arriba.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Hydroelectric_dam.svg/800px-Hydroelectric_dam.svg.png", caption="Esquema básico de una central")

with tab3:
    st.header("Panel de Datos en Tiempo Real")
    c1, c2, c3 = st.columns(3)
    c1.metric("Potencia Generada", "360 MW", "12%")
    c2.metric("Nivel Embalse", "85%", "Estable")
    c3.metric("Turbinas", "4 Operativas", "0 Fallos")
    
    st.subheader("Tabla Comparativa")
    st.table({
        "Variable": ["Altura Caída", "Capacidad", "Tipo"],
        "Valor": ["400 metros", "1000 GWh", "Bombeo Puro"]
    })

# Barra lateral informativa
st.sidebar.title("Sobre el Proyecto")
st.sidebar.write("Proyecto para la Feria de Ciencias 2026.")
st.sidebar.write("Autor: Parras")
st.sidebar.success("Estado: Conectado a la Red")
