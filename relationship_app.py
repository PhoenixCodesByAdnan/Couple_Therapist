import streamlit as st
from relationship_api import get_advice

# --- Page Config ---
st.set_page_config(
    page_title="HeartSpace — Couples Therapist",
    page_icon="💞",
    layout="centered"
)

# --- Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
}

.stApp {
    background: linear-gradient(135deg, #1a0a0f 0%, #2d0f1e 50%, #1a0a0f 100%);
    min-height: 100vh;
}

.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem;
    font-style: italic;
    color: #f4c2c2;
    text-align: center;
    margin-bottom: 0.2rem;
    letter-spacing: 1px;
}

.subtitle {
    text-align: center;
    color: #c89ca0;
    font-size: 1rem;
    font-weight: 300;
    margin-bottom: 2rem;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.advice-box {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(244,194,194,0.2);
    border-radius: 16px;
    padding: 1.5rem 2rem;
    margin-top: 1rem;
}

.activity-box {
    background: rgba(200,100,120,0.1);
    border-left: 3px solid #e07b8a;
    border-radius: 0 12px 12px 0;
    padding: 1rem 1.5rem;
    margin-top: 1rem;
}

.stButton > button {
    background: linear-gradient(135deg, #c0445a, #8b2a3a);
    color: white;
    border: none;
    border-radius: 50px;
    padding: 0.6rem 2.5rem;
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    font-weight: 500;
    letter-spacing: 1px;
    transition: all 0.3s ease;
    width: 100%;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #d45570, #a03347);
    transform: translateY(-1px);
    box-shadow: 0 8px 20px rgba(180, 60, 80, 0.4);
}

.stTextArea textarea {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(244,194,194,0.25) !important;
    border-radius: 12px !important;
    color: #f0dde0 !important;
    font-family: 'DM Sans', sans-serif !important;
}

.stSelectbox > div > div {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(244,194,194,0.25) !important;
    border-radius: 10px !important;
    color: #f0dde0 !important;
}

.stSlider > div > div {
    color: #f4c2c2;
}

label, .stMarkdown p {
    color: #d4a8b0 !important;
}

.divider {
    border: none;
    border-top: 1px solid rgba(244,194,194,0.15);
    margin: 1.5rem 0;
}

.step-label {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #c0445a;
    font-weight: 500;
    margin-bottom: 0.3rem;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="main-title">HeartSpace 💞</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your Private Couples Therapist</div>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- Session State init ---
if "profile_set" not in st.session_state:
    st.session_state.profile_set = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_age" not in st.session_state:
    st.session_state.user_age = 25
if "user_gender" not in st.session_state:
    st.session_state.user_gender = "Male"
if "relationship_duration" not in st.session_state:
    st.session_state.relationship_duration = "1-2 years"

# =====================
# STEP 1 — Profile Setup
# =====================
if not st.session_state.profile_set:
    st.markdown('<div class="step-label">Step 1 of 2 — About You</div>', unsafe_allow_html=True)
    st.markdown("### Tell me a little about yourself")
    st.markdown("*This helps me give you more personalised advice.*")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your first name", placeholder="e.g. Adnan")
        age = st.slider("Your age", min_value=16, max_value=70, value=25)

    with col2:
        gender = st.selectbox("I identify as", ["Male", "Female", "Non-binary / Other"])
        duration = st.selectbox("How long have you been together?", [
            "Less than 6 months",
            "6 months – 1 year",
            "1–2 years",
            "3–5 years",
            "5+ years",
            "Married"
        ])

    st.markdown("")
    if st.button("Continue to HeartSpace ➜"):
        if not name.strip():
            st.error("Please enter your name to continue.")
        else:
            st.session_state.profile_set = True
            st.session_state.user_name = name.strip()
            st.session_state.user_age = age
            st.session_state.user_gender = gender
            st.session_state.relationship_duration = duration
            st.rerun()

# =====================
# STEP 2 — Advice
# =====================
else:
    name = st.session_state.user_name
    age = st.session_state.user_age
    gender = st.session_state.user_gender
    duration = st.session_state.relationship_duration

    st.markdown(f"### Welcome, {name} 🌹")
    st.markdown(f"*{gender} · Age {age} · Together for {duration}*")
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.markdown('<div class="step-label">Step 2 of 2 — Your Situation</div>', unsafe_allow_html=True)
    st.markdown("### What's on your heart?")

    problem = st.text_area(
        "Describe your relationship challenge",
        placeholder="e.g. We argue a lot about small things and I feel we're growing apart...",
        height=150
    )

    topic = st.selectbox("Which area does this relate to most?", [
        "Communication & arguments",
        "Trust & jealousy",
        "Intimacy & connection",
        "Long distance",
        "Family & in-laws",
        "Work-life balance",
        "Growing apart",
        "Other"
    ])

    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("💬 Get Advice"):
            if not problem.strip():
                st.error("Please describe your situation first.")
            else:
                with st.spinner("Thinking through your situation with care..."):
                    result = get_advice(
                        name=name,
                        age=age,
                        gender=gender,
                        duration=duration,
                        problem=problem,
                        topic=topic
                    )

                st.markdown('<hr class="divider">', unsafe_allow_html=True)

                st.markdown("#### 🌸 Therapist's Advice")
                st.markdown(f'<div class="advice-box">{result["advice"]}</div>', unsafe_allow_html=True)

                st.markdown("#### 🎯 Suggested Activities for You Two")
                st.markdown(f'<div class="activity-box">{result["activities"]}</div>', unsafe_allow_html=True)

    with col_b:
        if st.button("← Change Profile"):
            st.session_state.profile_set = False
            st.rerun()
