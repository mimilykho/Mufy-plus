import streamlit as st
import base64

# 1. PAGE INITIALIZATION (Must be the very first command)
st.set_page_config(
    page_title="Cozy Focus Space",
    page_icon="🌸",
    layout="wide"
)

# 2. INS STYLE - CLEAN & MINIMAL PASTEL PRESETS
BACKGROUNDS = {
    "INS Cream Linen 🥛": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1920",
    "Soft Sage Leaf 🌱": "https://images.unsplash.com/photo-1540932239986-30128078f3c5?q=80&w=1920",
    "Minimalist Oatmeal 🥞": "https://images.unsplash.com/photo-1505691938895-1758d7feb511?q=80&w=1920",
    "INS Tulip Pink 🌷": "https://images.unsplash.com/photo-1533158326339-7f3cf2404354?q=80&w=1920",
    "Calm Powder Blue 🌊": "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=1920",
    "Muted Pastel Lavender 🪻": "https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?q=80&w=1920"
}

# 3. SIDEBAR CONTROLS
st.sidebar.title("🌸 Study Settings")
st.sidebar.markdown("Configure your perfect aesthetic study environment below.")
st.sidebar.markdown("---")

# --- Dynamic Background Chooser ---
bg_mode = st.sidebar.radio(
    "Background Source", 
    ["Preset Themes", "Paste an Image Link", "Upload From Computer"]
)

selected_bg_url = ""

if bg_mode == "Preset Themes":
    bg_choice = st.sidebar.selectbox("Select Theme Background", list(BACKGROUNDS.keys()))
    selected_bg_url = BACKGROUNDS[bg_choice]

elif bg_mode == "Paste an Image Link":
    custom_url = st.sidebar.text_input(
        "Paste your copied image link here:", 
        placeholder="https://example.com/your-image.jpg"
    )
    if custom_url:
        selected_bg_url = custom_url
    else:
        selected_bg_url = BACKGROUNDS["INS Cream Linen 🥛"]

else:
    uploaded_file = st.sidebar.file_uploader("Choose a photo from your device", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        file_bytes = uploaded_file.read()
        base64_image = base64.b64encode(file_bytes).decode("utf-8")
        selected_bg_url = f"data:image/jpeg;base64,{base64_image}"
    else:
        selected_bg_url = BACKGROUNDS["INS Cream Linen 🥛"] 

# --- Dynamic Motivation Customization ---
st.sidebar.subheader("✨ Motivation Word")
user_motivation = st.sidebar.text_input(
    "Type your motivation text:", 
    value="Keep blooming at your own pace! 🌸"
)

# --- Text Color Customization ---
st.sidebar.subheader("🎨 Text Styling")
user_text_color = st.sidebar.color_picker("Pick a Custom Text Color", "#5C677D")

# Inject CSS safely using double curly brackets to preserve style layouts
bg_css = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{selected_bg_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}
.cozy-card {{
    background-color: rgba(255, 255, 255, 0.88);
    padding: 35px;
    border-radius: 20px;
    color: {user_text_color} !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.5);
}}
.cozy-card h1, .cozy-card h2, .cozy-card h3, .cozy-card h4, .cozy-card p, .cozy-card span, .motivation-banner {{
    color: {user_text_color} !important;
    font-weight: 400;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}}
.motivation-banner {{
    font-size: 1.3rem;
    font-style: italic;
    text-align: center;
    margin: 20px 0px;
    padding: 12px;
    border-left: 3px solid {user_text_color};
    background-color: rgba(255, 255, 255, 0.4);
    border-radius: 4px;
}}
.app-button {{
    display: inline-block;
    width: 100%;
    text-align: center;
    padding: 14px 10px;
    background-color: rgba(255, 255, 255, 0.8);
    border: 1px solid {user_text_color};
    border-radius: 12px;
    text-decoration: none;
    font-size: 1.1rem;
    color: {user_text_color} !important;
    transition: all 0.2s ease-in-out;
    margin-top: 12px;
}}
.app-button:hover {{
    background-color: {user_text_color};
    color: #FFFFFF !important;
}}
</style>
"""
st.markdown(bg_css, unsafe_allow_html=True)


# 4. MAIN USER INTERFACE
st.markdown('<div class="cozy-card">', unsafe_allow_html=True)

st.title("🌱 Cozy Productivity Center")

if user_motivation:
    st.markdown(f'<div class="motivation-banner">✨ "{user_motivation}"</div>', unsafe_allow_html=True)

st.markdown("Your peaceful environment for deep work. Tap into your workspace apps seamlessly below.")
st.markdown("---")

# Main Hub Application Direct Launch Grid
st.subheader("🚀 Open Your Productivity Ecosystem")
st.markdown("Click an application below to open your tracking platform instantly in a new tab:")

# Grid layout with 3 columns for YPT, Forest, and Pomodoro
col_ypt, col_forest, col_pomo = st.columns(3)

with col_ypt:
    st.markdown("### 🔥 Yeolpumta")
    st.markdown("Join study groups and track real-time focus with friends globally.")
    st.markdown('<a href="https://www.yeolpumta.com/en/" target="_blank" class="app-button">⏱️ Open YPT</a>', unsafe_allow_html=True)

with col_forest:
    st.markdown("### 🌲 Forest App")
    st.markdown("Stay focused, plant virtual seeds, and grow your digital woods.")
    st.markdown('<a href="https://www.forestapp.cc/" target="_blank" class="app-button">🌱 Open Forest</a>', unsafe_allow_html=True)

with col_pomo:
    st.markdown("### 🍅 Pomodoro")
    st.markdown("Work efficiently using customizable 25-minute focus intervals.")
    st.markdown('<a href="https://pomofocus.io/" target="_blank" class="app-button">⏳ Open Pomofocus</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
   