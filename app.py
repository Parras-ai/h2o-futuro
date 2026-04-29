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
# 2. ESTILOS CSS MEJORADOS
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

[data-testid="stMetric"]::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 2px;
    background: linear-gradient(90deg, transparent, #00ffcc, transparent);
}

[data-testid="stMetricValue"] {
    font-family: 'Orbitron', monospace !important;
    color: #00ffcc !important;
    font-size: 1.8rem !important;
    text-shadow: 0 0 10px #00ffcc;
}

[data-testid="stMetricLabel"] { color: #88ffdd !important; letter-spacing: 1px; }
[data-testid="stMetricDelta"] { color: #00ff88 !important; }

.stTabs [data-baseweb="tab-list"] { background: #050505; border-bottom: 1px solid #00ffcc33; gap: 4px; }
.stTabs [data-baseweb="tab"] {
    font-family: 'Orbitron', monospace; color: #007755;
    border-radius: 6px 6px 0 0; letter-spacing: 1px;
    font-size: 0.75rem; padding: 8px 16px;
    border: 1px solid transparent; transition: all 0.3s;
}
.stTabs [aria-selected="true"] {
    background: #001a14 !important; color: #00ffcc !important;
    border: 1px solid #00ffcc44 !important;
    border-bottom-color: transparent !important;
    text-shadow: 0 0 8px #00ffcc;
}

[data-testid="stExpander"] {
    background: #0a1510; border: 1px solid #00ffcc22;
    border-radius: 8px; margin-bottom: 8px;
}
[data-testid="stExpander"]:hover { border-color: #00ffcc66; box-shadow: 0 0 15px #00ffcc11; }

[data-testid="stSidebar"] { background: linear-gradient(180deg, #030d0a, #050505); border-right: 1px solid #00ffcc22; }
[data-testid="stSidebar"] * { color: #88ffdd !important; }

hr { border-color: #00ffcc33 !important; box-shadow: 0 0 8px #00ffcc22; }

.stButton > button {
    font-family: 'Orbitron', monospace; background: transparent;
    color: #00ffcc; border: 1px solid #00ffcc;
    border-radius: 6px; letter-spacing: 2px; transition: all 0.3s;
}
.stButton > button:hover { background: #00ffcc22; box-shadow: 0 0 15px #00ffcc44; }

.progress-bar-container {
    background: #0a1a14; border: 1px solid #00ffcc33;
    border-radius: 20px; height: 16px; overflow: hidden; margin: 6px 0 14px 0; position: relative;
}
.progress-label {
    font-family: 'Share Tech Mono', monospace; font-size: 0.75rem;
    color: #88ffdd; display: flex; justify-content: space-between; margin-bottom: 2px;
}
.status-card {
    background: linear-gradient(135deg, #0a1a0f, #051008);
    border: 1px solid #00ff8844; border-radius: 10px;
    padding: 12px 18px; margin: 8px 0; display: flex; align-items: center; gap: 12px;
}
.status-dot {
    width: 10px; height: 10px; border-radius: 50%;
    background: #00ff88; box-shadow: 0 0 8px #00ff88;
    animation: pulse 2s infinite; flex-shrink: 0;
}
.status-dot.standby { background: #ffaa00; box-shadow: 0 0 8px #ffaa00; }
.status-dot.offline  { background: #ff3355; box-shadow: 0 0 8px #ff3355; }
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
@keyframes flicker { 0%, 95%, 100% { opacity: 1; } 96% { opacity: 0.8; } 98% { opacity: 0.7; } }
.header-glow { animation: flicker 8s infinite; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# 3. CABECERA
# ─────────────────────────────────────────────
st.markdown('<div class="header-glow">', unsafe_allow_html=True)
st.title("⚡ SISTEMA CENTRAL HIDROELÉCTRICA H2O")
st.markdown("""
<p style='text-align:center;color:#55bbaa;font-family:"Share Tech Mono",monospace;letter-spacing:2px;margin-top:-10px;'>
    INNOVACIÓN SOSTENIBLE · TAJO DE LA ENCANTADA · MÁLAGA
</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")

# ─────────────────────────────────────────────
# 4. PESTAÑAS
# ─────────────────────────────────────────────
tab_inicio, tab_ingenieria, tab_live = st.tabs([
    "🚀  VISIÓN GENERAL", "⚙️  ESQUEMA TÉCNICO", "📊  MONITORIZACIÓN LIVE"
])

# ══ TAB 1 ══════════════════════════════════════
with tab_inicio:
    st.header("Visión Global del Proyecto")
    col_txt, col_kpi = st.columns([3, 2], gap="large")

    with col_txt:
        st.markdown("""
        Esta central representa la **H2O-Futuro**, un prototipo avanzado de gestión energética.
        Inspirada en la central de bombeo del **Tajo de la Encantada** (Málaga), nuestro diseño
        integra tecnologías limpias para crear una **batería natural de alta eficiencia**.

        El sistema combina:
        - ⚡ Generación renovable mediante turbinas hidráulicas
        - 🌬️ Integración de excedentes eólicos para el bombeo
        - 🔄 Ciclos de carga/descarga controlados por IA
        - 📡 Monitorización SCADA en tiempo real
        """)
        st.info("💡 **Concepto Clave:** Sistema Hidroeólico con Almacenamiento por Bombeo y Recuperación SREC.")
        st.success("🟢 ESTADO GLOBAL: Sistema conectado y operativo a plena carga")

    with col_kpi:
        st.markdown("##### Datos del Proyecto")
        st.markdown("""
        <div style='background:#0a1a14;border:1px solid #00ffcc33;border-radius:10px;padding:18px;
                    font-family:"Share Tech Mono",monospace;font-size:0.85rem;line-height:2;'>
        🏔️ <b>Altitud embalse sup.</b><br>&nbsp;&nbsp;&nbsp;1 240 m.s.n.m.<br>
        💧 <b>Capacidad total</b><br>&nbsp;&nbsp;&nbsp;320 000 m³<br>
        ⚡ <b>Potencia instalada</b><br>&nbsp;&nbsp;&nbsp;370 MW<br>
        🔋 <b>Energía almacenable</b><br>&nbsp;&nbsp;&nbsp;1 800 MWh<br>
        🌿 <b>CO₂ evitado/año</b><br>&nbsp;&nbsp;&nbsp;~210 000 t
        </div>
        """, unsafe_allow_html=True)

# ══ TAB 2 ══════════════════════════════════════
with tab_ingenieria:
    st.header("Análisis de Componentes")

    componentes = [
        ("💧", "EMBALSES — Superior e Inferior",
         "Dos embalses a distintas alturas. El superior almacena energía potencial en horas de baja demanda (o excedente eólico) y el inferior la recoge tras la generación. Capacidad combinada: 320 000 m³."),
        ("🔴", "SENSORES IR — Control de Nivel",
         "Sensores de infrarrojos de precisión instalados en ambos embalses. Monitorizan el nivel de agua en tiempo real (resolución: ±2 cm), activando alarmas ante desbordamiento o nivel crítico."),
        ("🚇", "TUBERÍA TRANSPARENTE — Conducción Hidráulica",
         "Red de tuberías de alta presión con secciones transparentes para inspección visual. Diámetro nominal: 3,2 m. Caudal máximo: 120 m³/s. Pérdidas hidráulicas < 1,5%."),
        ("🌀", "TECNOLOGÍA SREC — Recuperación de Excedentes",
         "Sistema de recuperación de energía excedente (Surplus Recovery Energy Cycle). Maximiza el rendimiento durante fases de bombeo reversible, capturando hasta un 4% adicional de energía."),
        ("🖥️", "SCADA & APP DE CONTROL — Interfaz Digital",
         "Centro de mando digital con dashboard SCADA en tiempo real. Acceso remoto vía app móvil y web. Registros históricos, alertas push y control de actuadores con latencia < 200 ms."),
        ("🌬️", "INTEGRACIÓN EÓLICA — Bombeo Renovable",
         "Conexión directa con parques eólicos de la sierra. En horas de viento fuerte y baja demanda, el excedente eólico alimenta las bombas para elevar agua al embalse superior."),
    ]

    for icono, titulo, descripcion in componentes:
        with st.expander(f"{icono}  {titulo}"):
            st.markdown(f"<p style='color:#aaffd8;line-height:1.8;'>{descripcion}</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("##### Diagrama de flujo")
    st.markdown("""
    <div style='background:#050f0a;border:1px solid #00ffcc22;border-radius:10px;padding:20px;
                font-family:"Share Tech Mono",monospace;font-size:0.82rem;color:#55ddaa;text-align:center;line-height:2.5;'>
    🌬️ Viento / ☀️ Red eléctrica<br>
    ↓ <span style='color:#00ffcc'>bombeo reversible</span><br>
    💧 Embalse Superior (1 240 m)<br>
    ↓ <span style='color:#00ffcc'>caída libre (Δh = 580 m)</span><br>
    🌀 Turbinas Francis / SREC<br>
    ↓ <span style='color:#00ffcc'>generación</span><br>
    ⚡ Red Eléctrica Nacional<br>
    ↓ <span style='color:#00ffcc'>agua residual</span><br>
    💧 Embalse Inferior (660 m)
    </div>
    """, unsafe_allow_html=True)

# ══ TAB 3 ══════════════════════════════════════
with tab_live:
    st.header("Panel de Control — Tiempo Real")

    col_ctrl1, col_ctrl2, col_ctrl3 = st.columns([1, 1, 2])
    with col_ctrl1:
        auto_refresh = st.toggle("🔄 Auto-refresco (5s)", value=False)
    with col_ctrl2:
        if st.button("⟳  ACTUALIZAR"):
            st.rerun()
    with col_ctrl3:
        st.caption(f"🕐 Última actualización: {time.strftime('%H:%M:%S')}")

    st.markdown("---")

    # Inicializar session_state para deltas
    if "prev_potencia" not in st.session_state:
        st.session_state.prev_potencia   = 360.0
        st.session_state.prev_nivel_sup  = 85.0
        st.session_state.prev_nivel_inf  = 42.0
        st.session_state.prev_eficiencia = 98.5
        st.session_state.prev_frecuencia = 50.0
        st.session_state.prev_caudal     = 110.0

    # Generar nuevos valores
    potencia   = round(random.uniform(348, 372), 1)
    nivel_sup  = round(random.uniform(80,  92),  1)
    nivel_inf  = round(random.uniform(38,  55),  1)
    eficiencia = round(random.uniform(97.5, 99.5), 2)
    frecuencia = round(random.uniform(49.95, 50.05), 3)
    caudal     = round(random.uniform(100, 120), 1)

    delta_pot = round(potencia   - st.session_state.prev_potencia,   1)
    delta_efi = round(eficiencia - st.session_state.prev_eficiencia,  2)
    delta_cau = round(caudal     - st.session_state.prev_caudal,     1)

    # Guardar para la próxima iteración
    st.session_state.prev_potencia   = potencia
    st.session_state.prev_nivel_sup  = nivel_sup
    st.session_state.prev_nivel_inf  = nivel_inf
    st.session_state.prev_eficiencia = eficiencia
    st.session_state.prev_frecuencia = frecuencia
    st.session_state.prev_caudal     = caudal

    # KPIs
    c1, c2, c3 = st.columns(3)
    c1.metric("⚡ POTENCIA GENERADA", f"{potencia} MW",    f"{delta_pot:+.1f} MW")
    c2.metric("📊 EFICIENCIA GLOBAL", f"{eficiencia} %",   f"{delta_efi:+.2f} %")
    c3.metric("🌊 CAUDAL ACTIVO",     f"{caudal} m³/s",   f"{delta_cau:+.1f} m³/s")

    st.markdown("<br>", unsafe_allow_html=True)

    # Barras de nivel
    col_niv1, col_niv2 = st.columns(2)
    with col_niv1:
        st.markdown("##### 💧 Embalse Superior")
        color = "#00ffcc" if nivel_sup > 60 else "#ffaa00" if nivel_sup > 30 else "#ff3355"
        st.markdown(f"""
        <div class="progress-label"><span>Nivel</span><span>{nivel_sup}%</span></div>
        <div class="progress-bar-container">
          <div style="height:100%;border-radius:20px;width:{nivel_sup}%;
            background:linear-gradient(90deg,#003322,{color});box-shadow:0 0 10px {color}88;"></div>
        </div>""", unsafe_allow_html=True)

    with col_niv2:
        st.markdown("##### 💧 Embalse Inferior")
        color2 = "#00ccff" if nivel_inf < 70 else "#ffaa00"
        st.markdown(f"""
        <div class="progress-label"><span>Nivel</span><span>{nivel_inf}%</span></div>
        <div class="progress-bar-container">
          <div style="height:100%;border-radius:20px;width:{nivel_inf}%;
            background:linear-gradient(90deg,#001a33,{color2});box-shadow:0 0 10px {color2}88;"></div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("##### Estado de Componentes")

    componentes_estado = [
        ("🌀 Turbina 1",      "OPERATIVO", "",        "100%",  "Francis · 185 MW"),
        ("🌀 Turbina 2",      "OPERATIVO", "",        "100%",  "Francis · 185 MW"),
        ("⬆️ Bomba 1",        "STANDBY",   "standby", "0%",    "Reversible · Modo espera"),
        ("⬆️ Bomba 2",        "STANDBY",   "standby", "0%",    "Reversible · Modo espera"),
        ("🔴 Sensor Nivel S", "ACTIVO",    "",        "N/A",   "Embalse Superior · OK"),
        ("🔴 Sensor Nivel I", "ACTIVO",    "",        "N/A",   "Embalse Inferior · OK"),
        ("📡 SCADA Central",  "OPERATIVO", "",        "N/A",   f"Frec. red: {frecuencia} Hz"),
    ]

    color_estado = {"": "#00ff88", "standby": "#ffaa00", "offline": "#ff3355"}

    for nombre, estado, clase, carga, detalle in componentes_estado:
        col_est = color_estado[clase]
        st.markdown(f"""
        <div class="status-card">
          <div class="status-dot {clase}"></div>
          <div style="flex:1">
            <span style="font-family:'Orbitron',monospace;font-size:0.8rem;color:#00ffcc;">{nombre}</span>
            <span style="color:#333;margin:0 8px;">·</span>
            <span style="color:#88ffdd;font-size:0.8rem;">{detalle}</span>
          </div>
          <div style="text-align:right;min-width:110px;">
            <span style="font-size:0.72rem;color:#007755;">CARGA: {carga}</span><br>
            <span style="font-family:'Orbitron',monospace;font-size:0.7rem;color:{col_est};">{estado}</span>
          </div>
        </div>""", unsafe_allow_html=True)

    if auto_refresh:
        time.sleep(5)
        st.rerun()

# ─────────────────────────────────────────────
# 5. SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center;padding:10px 0 20px;'>
      <span style='font-family:"Orbitron",monospace;font-size:1.1rem;color:#00ffcc;text-shadow:0 0 10px #00ffcc;'>
        ⚡ H2O-FUTURO
      </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**Autor:** Colegio Bética-Mudarra")
    st.markdown("**Año:** 2025")
    st.markdown("---")
    st.subheader("📱 Acceso Rápido")
    # URL corregida (sin saltos de línea)
    st.image(
        "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://h2o-futuro.streamlit.app",
        caption="Escanea para acceder",
        use_container_width=True
    )
    st.markdown("---")
    st.subheader("📈 Resumen")
    st.markdown(f"""
    <div style='font-family:"Share Tech Mono",monospace;font-size:0.8rem;line-height:2;color:#88ffdd;'>
    ⚡ Potencia: <b style='color:#00ffcc'>{st.session_state.prev_potencia} MW</b><br>
    💧 Emb. Sup.: <b style='color:#00ffcc'>{st.session_state.prev_nivel_sup}%</b><br>
    💧 Emb. Inf.: <b style='color:#00ccff'>{st.session_state.prev_nivel_inf}%</b><br>
    ✅ Eficiencia: <b style='color:#00ff88'>{st.session_state.prev_eficiencia}%</b>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.caption("Sistema H2O v2.0 · Datos simulados con fines académicos")
