import streamlit as st
import random
from datetime import date

# --------------------
# Page config
# --------------------
st.set_page_config(
    page_title="Is it today?",
    page_icon="🌙",
    layout="centered"
)

# --------------------
# CSS / Moon theme styling
# --------------------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(180deg, #0b0f1a 0%, #121826 100%);
        color: #e6e6e6;
    }

    .stApp {
        font-family: 'Inter', sans-serif;
        animation: fadeIn 1.5s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    h1 {
        font-weight: 500;
        letter-spacing: 0.02em;
    }

    .stCaption {
        color: #b0b3c6;
    }

    button {
        border-radius: 12px !important;
        background-color: #1c2233 !important;
        color: #e6e6e6 !important;
        border: 1px solid #2a314a !important;
        transition: all 0.2s ease-in-out;
    }

    button:hover {
        background-color: #232a40 !important;
        transform: scale(1.05);
    }

    .stExpander {
        background-color: #141a2a;
        border-radius: 16px;
        border: 1px solid #232a40;
    }

    .date-box {
        background-color: #f5d76e;
        color: #1c1c1c;
        border-radius: 16px;
        padding: 25px;
        font-size: 32px;
        text-align: center;
        margin: 20px 0px;
        font-weight: 600;
        position: relative;
    }

    /* Orbiting moon animation */
    .orbit-container {
        position: relative;
        width: 100%;
        height: 80px;
        margin-top: -60px;
    }

    .orbit-moon {
        position: absolute;
        left: 50%;
        top: 50%;
        font-size: 28px;
        transform-origin: -60px 0px;  /* radius of orbit */
        animation: orbit 15s linear infinite;
    }

    @keyframes orbit {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------
# Title & context
# --------------------
st.title("🌙 Is it today?")
st.caption("For Sathya. A small app that checks whether it’s your birthday.")

# --------------------
# Today's date box
# --------------------
today = date.today()
today_str = today.strftime("%A, %B %d, %Y")

st.markdown(
    f"""
    <div class="date-box">
        🌑 🌒 {today_str} 🌕 🌗
    </div>
    """,
    unsafe_allow_html=True
)

# Orbiting moon emoji
st.markdown("""
<div class="orbit-container">
    <div class="orbit-moon">🌙</div>
</div>
""", unsafe_allow_html=True)

st.write("Is it today?")

# --------------------
# Rotating quotes
# --------------------
neutral_quotes = [
    "The moon keeps watch.",
    "Time drifts quietly.",
    "All is still tonight.",
    "The sky waits patiently.",
    "Observing the silent night.",
    "The stars wink softly.",
    "The night whispers nothing.",
]

yes_quotes = [
    "Today is your day. 🌕",
    "The moon is full and bright for you.",
    "The calendar agrees. 🎂",
    "The night celebrates quietly for you.",
]

no_quotes = [
    "Still quiet. 🌙",
    "The moon observes.",
    "Another night, another orbit.",
    "Patience. The sky waits.",
]

# --------------------
# Buttons and reactive message
# --------------------
col1, col2 = st.columns(2)

clicked_yes = col1.button("Yes", key="yes_btn")
clicked_no = col2.button("No", key="no_btn")

# message display
random.seed(today.toordinal())

if clicked_yes:
    st.markdown(
        f"<div style='text-align:center; opacity:0.85;'>{random.choice(yes_quotes)}</div>",
        unsafe_allow_html=True
    )
elif clicked_no:
    st.markdown(
        f"<div style='text-align:center; opacity:0.85;'>{random.choice(no_quotes)}</div>",
        unsafe_allow_html=True
    )
else:
    st.markdown(
        f"<div style='text-align:center; opacity:0.85;'>{random.choice(neutral_quotes)}</div>",
        unsafe_allow_html=True
    )

# --------------------
# Moon phase (symbolic)
# --------------------
day = today.day
if day <= 7:
    phase = "🌑 New moon"
elif day <= 14:
    phase = "🌓 First quarter"
elif day <= 21:
    phase = "🌕 Full moon"
else:
    phase = "🌗 Waning moon"

st.caption(phase)

# --------------------
# Streak visualization
# --------------------
START_DATE = date.today()
days_checked = (today - START_DATE).days

streak_moons = "🌑🌒🌓🌔🌕🌖🌗🌘"
streak_display = streak_moons[: (days_checked % len(streak_moons)) + 1]

st.caption(f"🌒 Day {days_checked} of checking {streak_display}")

st.markdown("---")

# --------------------
# Why this exists (personal quote)
# --------------------
with st.expander("Why this exists"):
    st.write(
        "You don’t make a big deal of birthdays, and that’s fine.  \n"
        "I still like to remember them, quietly, like the moon keeps its orbit every night."
    )

# --------------------
# Visual flourish
# --------------------
st.markdown(
    "<div style='text-align:center; opacity:0.3; font-size:22px;'>☽</div>",
    unsafe_allow_html=True
)

# --------------------
# Footer
# --------------------
st.markdown(
    "<div style='text-align: center; opacity: 0.6; margin-top: 40px;'>"
    "Still orbiting."
    "</div>",
    unsafe_allow_html=True
)
