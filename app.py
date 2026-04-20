import streamlit as st

# Configuración básica
st.set_page_config(page_title="Hidroeléctrica H2O", layout="centered")

# Título y encabezado
st.title("🌊 Hidroeléctrica del Futuro H2O")
st.subheader("Proyecto Tecnológico - Feria de Ciencias")

# Menú lateral
menu = st.sidebar.selectbox("Navegación", ["Inicio", "Funcionamiento", "Datos Técnicos"])

if menu == "Inicio":
    st.write("Bienvenido a la plataforma oficial de la Hidroeléctrica H2O.")
    st.image("https://images.unsplash.com/photo-1590069261209-48e3b267514f?q=80&w=800")
    st.info("Explora cómo transformamos la energía del agua en electricidad limpia.")

elif menu == "Funcionamiento":
    st.header("¿Cómo funciona?")
    st.write("1. **Captación:** El agua es retenida en el embalse.")
    st.write("2. **Generación:** El flujo mueve las turbinas.")
    st.write("3. **Distribución:** La energía llega a las ciudades.")

elif menu == "Datos Técnicos":
    st.header("Estadísticas del Sistema")
    st.metric(label="Energía Generada", value="120 MWh", delta="15%")
    st.metric(label="Nivel de Agua", value="85%")
