import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA: Diseño ancho para tablet
st.set_page_config(
    page_title="H2O - Central Futurista v2.0",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ESTILOS CSS: El "Toque LED" y Futurista
st.markdown("""
    <style>
    /* Fondo oscuro profundo y texto cian neón */
    .stApp {
        background-color: #050505;
        color: #00ffcc;
        font-family: 'Courier New', monospace;
    }
    
    /* Títulos principales con efecto neón brillante */
    h1 {
        color: #00ffcc;
        text-shadow: 0 0 15px #00ffcc, 0 0 5px #ffffff;
        text-align: center;
        padding-bottom: 20px;
    }
    
    /* Subtítulos en fucsia neón */
    h2, h3 {
        color: #ff00ff;
        text-shadow: 0 0 10px #ff00ff;
        padding-top: 20px;
    }
    
    /* Tarjetas de métricas: Paneles de control */
    .stMetric {
        background-color: #111111;
        border: 2px solid #00ffcc;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.2);
        transition: all 0.3s ease;
    }
    .stMetric:hover {
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.4);
        transform: translateY(-5px);
    }
    
    /* Estilo para los textos informativos */
    .stInfo {
        background-color: rgba(0, 255, 255, 0.1);
        color: #ffffff;
        border-left: 5px solid #00ffcc;
        border-radius: 5px;
    }

    /* Estilo para las secciones desplegables */
    .stSidebar .stMarkdown {
        color: #ffffff;
    }
    
    /* Ocultar menú de Streamlit para modo presentación */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. TÍTULO PRINCIPAL Y CABECERA
st.title("⚡ SISTEMA CENTRAL HIDROELÉCTRICA H2O")
st.markdown("<h3 style='text-align: center; color: #ffffff;'>Innovación Sostenible Inspirada en el Tajo de la Encantada</h3>", unsafe_allow_html=True)
st.markdown("---")

# 4. ESTRUCTURA DE PESTAÑAS (TABS)
tab_inicio, tab_ingenieria, tab_live = st.tabs(["🚀 INICIO / VISIÓN GENERAL", "⚙️ ESQUEMA TÉCNICO", "📊 MONITORIZACIÓN LIVE"])

# --- PESTAÑA 1: INICIO (Recrea la Imagen 1) ---
with tab_inicio:
    st.header("Modo Presentación: Visión Global")
    
    col_text, col_status = st.columns([2, 1])
    
    with col_text:
        st.write("""
        Esta central representa la **H2O-Futuro**, un prototipo avanzado de gestión energética.
        Inspirada en la central de bombeo del Tajo de la Encantada (Málaga), nuestro diseño
        integra tecnologías limpias para crear una **batería natural de alta eficiencia**.
        
        Nuestra misión: Transformar la energía hidráulica en una red inteligente y sostenible para Andalucía.
        """)
        st.info("💡 **Concepto Clave:** Sistema Hidroeólico con Almacenamiento por Bombeo y Recuperación SREC.")
    
    with col_status:
        st.write("### ESTADO DEL SISTEMA")
        st.success("🟢 ONLINE - Red Conectada")
        st.warning("⚠️ Modo Feria Activado")

# --- PESTAÑA 2: INGENIERÍA (Recrea la Imagen 2) ---
with tab_ingenieria:
    st.header("Análisis de Componentes y Flujo")
    st.write("Explora cada elemento del sistema detallado en nuestro esquema original.")

    # Usamos expanders para cada componente detallado
    with st.expander("💧 EMBALSES (Superior e Inferior)"):
        st.write("""
        **Nuestra estructura:** Dos embalses a distintas alturas.
        - **Embalse Superior (H2O-UP):** Almacena agua en horas de baja demanda.
        - **Embalse Inferior (H2O-DOWN):** Recoge el agua tras la generación.
        **Función:** Actúan como una 'batería' de energía potencial.
        """)

    with st.expander("🆔 SENSORES DE INFRARROJOS (Control de Nivel)"):
        st.write("""
        **Tecnología:** Sensores de precisión para monitorear el nivel de agua en tiempo real.
        **Uso:** Previenen desbordamientos y optimizan los ciclos de bombeo y generación.
        **Integración:** Conectados directamente a la App de Control.
        """)

    with st.expander("🚇 TUBERÍA TRANSPARENTE (Conducción Hidráulica)"):
        st.write("""
        **Diseño:** Tuberías de alta presión y transparencia para inspección visual y didáctica.
        **Función:** Transportan el agua entre embalses con mínima pérdida por fricción.
        """)

    with st.expander("🌀 TURBINAS Y RECUPERADOR (Generación y Bombeo SREC)"):
        st.write("""
        **El Corazón de la Central:**
        - **Turbinas de Alta Eficiencia:** Generan electricidad en horas punta.
        - **Modo Bombeo SREC:** El mismo sistema actúa como bomba para subir el agua.
        - **SREC (Recuperación):** Sistema de recuperación de energía excedente para maximizar el rendimiento global.
        """)

    with st.expander("📱 APP DE CONTROL (Interfaz Digital)"):
        st.write("""
        **Centro de Mando:** Interfaz móvil y web para el monitoreo de todos los parámetros: potencia, nivel de agua, estado de turbinas y control de flujo.
        """)

# --- PESTAÑA 3: MONITORIZACIÓN LIVE (Panel de Datos) ---
with tab_live:
    st.header("Panel de Control Energético (SIMULACIÓN)")
    st.write("Datos técnicos simulados en tiempo real para la presentación.")
    
    # Fila de métricas clave (Los "paneles LED")
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    row1_col1.metric("POTENCIA ACTUAL", "1.2 GW", "12%", help="Variación respecto a la hora anterior")
    row1_col2.metric("NIVEL EMBALSE (SUP)", "85%", "Estable", help="Capacidad total de almacenamiento")
    row1_col3.metric("EFICIENCIA SREC", "98.5%", "Aumentando", help="Rendimiento de la recuperación energética")

    # Tabla detallada (Más info visual)
    st.subheader("Estado de Componentes")
    st.table({
        "Componente": ["Turbina 1", "Turbina 2", "Bomba 1", "Sensor Nivel UP", "Tubería Principal"],
        "Estado": ["OPERATIVA", "OPERATIVA", "STANDBY", "OPERATIVO", "FLUJO ÓPTIMO"],
        "Carga": ["100%", "100%", "0%", "N/A", "100%"]
    })

# 5. BARRA LATERAL (Sidebar)
st.sidebar.title("🚨 PANEL DE CONTROL CENTRAL")
st.sidebar.markdown("---")
st.sidebar.write("**Autor:** Parras AI")
st.sidebar.write("**Proyecto:** Feria de Ciencias 2026")
st.sidebar.markdown("---")
st.sidebar.write("**Seguridad:** Acceso Restringido")

# Botón interactivo (funciona seguro)
if st.sidebar.button("EJECUTAR DIAGNÓSTICO DEL SISTEMA"):
    st.sidebar.success("✅ Diagnóstico Completado: SISTEMA SIN ERRORES")
