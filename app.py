import streamlit as st
import time
import random

# ─────────────────────────────────────────────
# 1. CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="H2O — Central Hidroeléctrica",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# 2. ESTILOS CSS (Diseño Cyberpunk / LED)
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');

.stApp {
    background: radial-gradient(ellipse at 20% 50%, #001a1a 0%, #050505 60%);
    color: #c0fff5;
    font-family: 'Share Tech Mono', monospace;
}

.stApp::before {
    content: '';
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(
        0deg, transparent, transparent 2px,
        rgba(0, 255, 200, 0.015) 2px, rgba(0, 255, 200, 0.015) 4px
    );
    pointer-events: none;
    z-index: 9999;
}

h1 {
    font-family: 'Orbitron', monospace !important;
    color: #00ffcc !important;
    text-shadow: 0 0 20px #00ffcc, 0 0 40px #00ffcc55;
    text-align: center;
    letter-spacing: 4px;
    font-size: 2.2rem !important;
    padding-bottom: 10px;
}

h2, h3 {
    font-family: 'Orbitron', monospace !important;
    color: #00ccff !important;
    text-shadow: 0 0 10px #00ccff88;
    letter-spacing: 2px;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg, #0a1a1a, #001515);
    border: 1px solid #00ffcc44;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 0 20px #00ffcc22, inset 0 0 20px #00000066;
    position: relative;
    overflow: hidden;
}

[data-testid="stMetricValue"] {
    font-family: 'Orbitron', monospace !important;
    color: #00ffcc !important;
    font-size: 1.8rem !important;
    text-shadow: 0 0 10px #00ffcc;
}

.stTabs [aria-selected="true"] {
    background: #001a14 !important; color: #00ffcc !important;
    text-shadow: 0 0 8px #00ffcc;
}

.status-dot {
    width: 10px; height: 10px; border-radius: 50%;
    background: #00ff88; box-shadow: 0 0 8px #00ff88;
    animation: pulse 2s infinite;
}
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
</style>
""", unsafe_allow_html=True)

# 3. CABECERA (Título actualizado)
st.title("⚡ Hidroeléctrica FuturH2O")
st.markdown("""
<p style='text-align:center;color:#55bbaa;font-family:"Share Tech Mono",monospace;letter-spacing:2px;margin-top:-10px;'>
    COLEGIO BÉTICA-MUDARRA · TAJO DE LA ENCANTADA · MÁLAGA
</p>
""", unsafe_allow_html=True)
st.markdown("---")

# 4. PESTAÑAS
tab_inicio, tab_ingenieria, tab_live = st.tabs([
    "🚀  VISIÓN GENERAL", "⚙️  ESQUEMA TÉCNICO", "📊  MONITORIZACIÓN LIVE"
])

with tab_inicio:
    st.header("Visión Global del Proyecto")
    col_txt, col_kpi = st.columns([3, 2], gap="large")
    with col_txt:
        st.markdown("""
        Esta central representa la **H2O-Futuro**, un prototipo avanzado de gestión energética.
        Inspirada en el **Tajo de la Encantada**, nuestro diseño crea una **batería natural de alta eficiencia**.
        """)
        st.info("💡 **Concepto Clave:** Almacenamiento por Bombeo y Recuperación SREC.")

with tab_ingenieria:
    st.header("Análisis de Componentes")
    componentes = [
        ("💧", "EMBALSES", "Gestión de energía potencial entre niveles superior e inferior."),
        ("🔴", "SENSORES IR", "Monitorización infrarroja de nivel con precisión milimétrica."),
        ("🚇", "CONDUCCIÓN", "Tubería transparente de alta presión para inspección de flujo."),
        ("🌀", "SREC", "Sistema de Recuperación de Energía para máxima eficiencia energética."),
        ("🖥️", "SCADA", "Interfaz digital de control y monitorización remota.")
    ]
    for icono, titulo, desc in componentes:
        with st.expander(f"{icono} {titulo}"):
            st.write(desc)

with tab_live:
    st.header("Panel de Control — Tiempo Real")
    
    if "prev_potencia" not in st.session_state:
        st.session_state.prev_potencia = 360.0

    potencia = round(random.uniform(348, 372), 1)
    delta_pot = round(potencia - st.session_state.prev_potencia, 1)
    st.session_state.prev_potencia = potencia

    c1, c2, c3 = st.columns(3)
    c1.metric("⚡ POTENCIA GENERADA", f"{potencia} MW", f"{delta_pot:+.1f} MW")
    c2.metric("📊 EFICIENCIA GLOBAL", f"{random.uniform(97.5, 99.5):.2f} %")
    c3.metric("🌊 CAUDAL ACTIVO", f"{random.uniform(100, 120):.1f} m³/s")

    if st.button("⟳ ACTUALIZAR DATOS"):
        st.rerun()

# 5. BARRA LATERAL (Sidebar)
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>⚡ H2O-FUTURO</h2>", unsafe_allow_html=True)
    st.markdown("**Autor:** Colegio Bética-Mudarra")
    st.markdown("**Centro:** Colegio Bética-Mudarra")
    st.markdown("---")
    st.subheader("📱 Acceso Rápido")
    st.image("https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://h2o-futuro.streamlit.app")
    st.caption("Sistema FuturH2O v2.0 · Colegio Bética-Mudarra")
