import streamlit as st

# Configuración de página: layout 'wide' para aprovechar toda la pantalla
st.set_page_config(page_title="Hidroeléctrica H2O", layout="wide")

# Estilos CSS para un look "Tecnológico/Gamer"
st.markdown("""
    <style>
    .stApp { background-color: #0a0c10; color: #e0e0e0; }
    h1 { color: #00ffcc; text-align: center; }
    h2 { color: #00ffcc; }
    .stMetric { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.title("🌊 Central Hidroeléctrica H2O: Tajo de la Encantada")
st.markdown("---")

# Pestañas para organizar la información
tab_inicio, tab_funcionamiento, tab_datos = st.tabs(["🏗️ Visión General", "🔍 Detalles Técnicos", "📊 Panel de Control"])

with tab_inicio:
    st.header("Hidroeléctrica del Futuro H2O")
    # Imagen 1: La que es tipo "nicho" o visión global
    st.image("nicho.png", caption="Inspirada en la Central del Tajo de la Encantada, Málaga", use_container_width=True)
    st.write("### Innovación Sostenible para Andalucía")
    st.info("Un sistema integrado que combina energía fotovoltaica, sensores de infrarrojos y recuperación de energía SREC para maximizar la eficiencia.")

with tab_funcionamiento:
    st.header("Esquema Detallado del Proyecto")
    # Imagen 2: La que tiene todas las etiquetas y flechas
    st.image("detalle.png", caption="Componentes técnicos del sistema", use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Componentes Clave")
        st.write("✅ **Embalses:** Superior e Inferior para gestión de bombeo.")
        st.write("✅ **Conducción:** Tuberías transparentes de alta presión.")
        st.write("✅ **Generación:** Turbinas de alta eficiencia.")
    with col2:
        st.subheader("Control Digital")
        st.write("✅ **Sensores:** Infrarrojos para monitoreo en tiempo real.")
        st.write("✅ **APP:** Centro de mando digital desde cualquier dispositivo.")
        st.write("✅ **SREC:** Sistema de recuperación de energía.")

with tab_datos:
    st.header("Datos de Producción en Tiempo Real")
    c1, c2, c3 = st.columns(3)
    c1.metric("Potencia Generada", "360 MW", "12%")
    c2.metric("Nivel Embalse", "85%", "Estable")
    c3.metric("Turbinas", "4 Activas", "0 Fallos")
    
    st.subheader("Tabla de Especificaciones")
    st.table({
        "Variable": ["Altura de Caída", "Capacidad", "Estado del Sensor"],
        "Detalle": ["400 metros", "1000 GWh", "OPERATIVO"]
    })

# Barra lateral para información rápida
st.sidebar.title("Sobre el Proyecto")
st.sidebar.write("Proyecto presentado para la Feria de Ciencias.")
st.sidebar.write("Autor: Parras")
st.sidebar.success("Estado de conexión: Conectado a la Red")

