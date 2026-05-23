import streamlit as st
#import numpy as np

st.write("# Welcome to my app!")

# ── Page configuration ─────────────────────────────────────────────────────────
st.set_page_config(
    page_title="BMI Health Calculator",
    page_icon="⚕️",
    layout="centered",
)

# ── WHO BMI Classification ─────────────────────────────────────────────────────
WHO_CLASSES = [
    # (label,              min_bmi, max_bmi,  hex_color,   dot_color)
    ("Underweight",         0.0,    18.49,   "#dbeafe",   "#3b82f6"),
    ("Normal weight",      18.5,    22.99,   "#dcfce7",   "#22c55e"),
    ("Overweight",         23.0,    24.99,   "#fef9c3",   "#eab308"),
    ("Obese — Class I",    25.0,    29.99,   "#ffedd5",   "#f97316"),
    ("Obese — Class II",   30.0,    39.99,   "#fee2e2",   "#ef4444"),
    ("Obese — Class III",  40.0,   999.99,   "#fce7f3",   "#db2777"),
]


def classify_bmi(bmi: float) -> tuple[str, str, str]:
    """Return (category_label, bg_hex, dot_hex) for a given BMI value."""
    for label, lo, hi, bg, dot in WHO_CLASSES:
        if lo <= bmi <= hi:
            return label, bg, dot
    return "Obese — Class III", "#fce7f3", "#db2777"


def bmi_scale_pct(bmi: float) -> float:
    """Map BMI to a 0–100 percentage position on the visual scale bar.
    The scale is anchored: 10 → 0%, 40 → 100% (clamped).
    """
    pct = (bmi - 10) / (40 - 10) * 100
    return max(2, min(98, pct))


def health_advice(category: str) -> str:
    advice = {
        "Underweight":        "Consider consulting a nutritionist to reach a healthy weight through a balanced caloric intake.",
        "Normal weight":      "Excellent — maintain your current lifestyle with regular physical activity and a balanced diet.",
        "Overweight":         "Moderate dietary adjustments and increased aerobic activity are recommended.",
        "Obese — Class I":    "Consultation with a healthcare provider is advisable to establish a structured weight-management plan.",
        "Obese — Class II":   "Medical supervision is strongly recommended. Lifestyle interventions and clinical support can be highly effective.",
        "Obese — Class III":  "Please seek immediate medical guidance. Specialised clinical intervention is recommended.",
    }
    return advice.get(category, "")


# ── App Header ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <h1>⚕️ BMI Health Calculator</h1>
    <p>Body Mass Index assessment based on WHO classification standards</p>
</div>
""", unsafe_allow_html=True)

# ── Input Form ────────────────────────────────────────────────────────────────
st.markdown('👤 Personal Information')

col_name, col_phone = st.columns(2)
with col_name:
    name: str = st.text_input("Full name", placeholder="e.g. Alice Johnson")
with col_phone:
    phone: str = st.text_input("Phone number", placeholder="e.g. +66 81 234 5678")

col_age, col_gender = st.columns(2)
with col_age:
    age: int = st.number_input("Age (years)", min_value=1, max_value=120, value=25, step=1)
with col_gender:
    unit_system: str = st.radio("Unit system", ["Metric (kg / cm)", "Imperial (lb / in)"], horizontal=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card"><div class="card-title">📏 Body Measurements</div>', unsafe_allow_html=True)

col_w, col_h = st.columns(2)

if unit_system.startswith("Metric"):
    with col_w:
        weight_kg: float = st.number_input("Weight (kg)", min_value=1.0, max_value=500.0, value=70.0, step=0.5)
    with col_h:
        height_cm: float = st.number_input("Height (cm)", min_value=30.0, max_value=300.0, value=170.0, step=0.5)
else:
    with col_w:
        weight_lb: float = st.number_input("Weight (lb)", min_value=2.0, max_value=1100.0, value=154.0, step=1.0)
        weight_kg = weight_lb * 0.453592
    with col_h:
        height_in: float = st.number_input("Height (in)", min_value=12.0, max_value=120.0, value=67.0, step=0.5)
        height_cm = height_in * 2.54

st.markdown('</div>', unsafe_allow_html=True)

calculate = st.button("Calculate BMI →")

# ── Validation & Computation ──────────────────────────────────────────────────
if calculate:
    errors = []
    if not name.strip():
        errors.append("Full name is required.")
    if not phone.strip():
        errors.append("Phone number is required.")
    if weight_kg <= 0:
        errors.append("Weight must be a positive value.")
    if height_cm <= 0:
        errors.append("Height must be a positive value.")

    if errors:
        for e in errors:
            st.error(e)
    else:
        # ── Core BMI calculation ──────────────────────────────────────────────
        # Formula (WHO): BMI = mass(kg) / height(m)²
        height_m: float = height_cm / 100.0
        bmi: float = weight_kg / (height_m ** 2)
        bmi_rounded: float = round(bmi, 1)

        category, bg_color, dot_color = classify_bmi(bmi_rounded)
        marker_pct = bmi_scale_pct(bmi_rounded)
        advice = health_advice(category)
        is_normal = category == "Normal weight"

        # ── Result panel ─────────────────────────────────────────────────────
        status_icon = "✅" if is_normal else ("⚠️" if bmi_rounded < 25 else "🔴")

        st.markdown(f"""
        <div class="result-panel" style="background:{bg_color};">
            <div class="result-name" style="color:{dot_color};">{status_icon} {name.strip()}</div>
            <div class="result-bmi" style="color:#1a3a2a;">{bmi_rounded}</div>
            <div style="font-size:0.85rem;color:#5a7a6a;margin-bottom:0.2rem;">kg / m²</div>
            <div class="result-category" style="color:{dot_color};">{category}</div>
            <div class="result-note" style="color:#1a3a2a;">{advice}</div>

      
        </div>
        """, unsafe_allow_html=True)

        # ── Summary metrics ───────────────────────────────────────────────────
        st.markdown("---")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Age",    f"{age} yrs")
        m2.metric("Weight", f"{weight_kg:.1f} kg")
        m3.metric("Height", f"{height_cm:.1f} cm")
        m4.metric("BMI",    f"{bmi_rounded}")

        # ── WHO Classification Table ──────────────────────────────────────────
        st.markdown('<div class="card" style="margin-top:1.4rem;">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">📊 WHO BMI Classification Reference</div>', unsafe_allow_html=True)

        rows = ""
        for label, lo, hi, _, dot in WHO_CLASSES:
            hi_str = f"≥ {lo:.1f}" if hi > 100 else f"{lo:.1f} – {hi:.1f}"
            is_current = label == category
            row_class = "highlight" if is_current else ""
            arrow = " ◀ your result" if is_current else ""
            rows += f"""
            <tr class="{row_class}">
                <td><span class="dot" style="background:{dot};"></span>{label}{arrow}</td>
                <td>{hi_str}</td>
            </tr>"""

        st.markdown(f"""
        <table class="who-table">
            <thead>
                <tr>
                    <th>Category</th>
                    <th>BMI Range (kg/m²)</th>
                </tr>
            </thead>
            <tbody>{rows}</tbody>
        </table>
        <p style="font-size:0.75rem;color:#8aaa9a;margin-top:0.8rem;">
            Source: World Health Organization (2000). <em>Obesity: Preventing and Managing the Global Epidemic.</em>
            WHO Technical Report Series No. 894.
        </p>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)