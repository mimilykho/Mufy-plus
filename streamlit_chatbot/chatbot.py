import streamlit as st
import base64

# 1. PAGE INITIALIZATION (Must be the very first Streamlit command)
st.set_page_config(
    page_title="Cozy Focus Space",
    page_icon="🌸",
    layout="wide"
)

# 2. INS STYLE - CLEAN, SIMPLE, & MINIMAL PASTEL PRESETS
BACKGROUNDS = {
    "INS Cream Linen 🥛": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1920",
    "Soft Sage Leaf 🌱": "https://images.unsplash.com/photo-1540932239986-30128078f3c5?q=80&w=1920",
    "Minimalist Oatmeal 🥞": "https://images.unsplash.com/photo-1505691938895-1758d7feb511?q=80&w=1920",
    "INS Tulip Pink 🌷": "https://images.unsplash.com/photo-1533158326339-7f3cf2404354?q=80&w=1920",
    "Calm Powder Blue 🌊": "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=1920",
    "Muted Pastel Lavender 🪻": "https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?q=80&w=1920"
}

# High-focus, peace-inducing audio tracks for studying
MUSIC_TRACKS = {
    "🎹 Soft Ghibli Piano (Study Instrumentals)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3",
    "🌧️ Tokyo Cafe Rain (Focus Background Noise)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "🌳 Cozy Forest Campfire (Nature Ambience)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3",
    "🧸 Sweet Music Box (Calm Mindset)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    "🧠 Focus Alpha Waves (Binaural Beats)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3"
}

# 3. SIDEBAR CONTROLS
st.sidebar.title("🌸 Study Settings")
st.sidebar.markdown("Configure your perfect aesthetic study environment below.")
st.sidebar.markdown("---")

# --- Dynamic Background Chooser ---
st.sidebar.subheader("🖼️ Choose Vibe")
bg_mode = st.sidebar.radio(
    "Background Source", 
    ["Preset Themes", "Upload My Own"]
)

selected_bg_url = ""

if bg_mode == "Preset Themes":
    bg_choice = st.sidebar.selectbox("Select Theme Background", list(BACKGROUNDS.keys()))
    selected_bg_url = BACKGROUNDS[bg_choice]
else:
    uploaded_file = st.sidebar.file_uploader("Upload a cute/peaceful photo", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        file_bytes = uploaded_file.read()
        base64_image = base64.b64encode(file_bytes).decode("utf-8")
        selected_bg_url = f"data:image/jpeg;base64,{base64_image}"
    else:
        selected_bg_url = BACKGROUNDS["INS Cream Linen 🥛"] 
        st.sidebar.info("Showing default preset until you upload a photo.")


# --- Dynamic Motivation Customization ---
st.sidebar.subheader("✨ Motivation Word")
user_motivation = st.sidebar.text_input(
    "Type your motivation text:", 
    value="Keep blooming at your own pace! 🌸"
)

# --- Text Color Customization ---
st.sidebar.subheader("🎨 Text Styling")
user_text_color = st.sidebar.color_picker("Pick a Custom Text Color", "#5C677D")

# Inject CSS safely using double curly brackets to prevent Python layout parsing syntax issues
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
/* Clean, soft glassmorphism card for INS aesthetic */
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
    box-shadow: 0 4px 15px rgba(0,0,0,0.04);
}}
</style>
"""
st.markdown(bg_css, unsafe_allow_html=True)


# --- Music Toggle System ---
st.sidebar.subheader("🎵 Study Music")
music_on = st.sidebar.toggle("Turn On Music", value=False)

if music_on:
    track_choice = st.sidebar.selectbox("Select Study Sound", list(MUSIC_TRACKS.keys()))
    st.sidebar.audio(MUSIC_TRACKS[track_choice], format="audio/mp3", loop=True)
else:
    st.sidebar.info("Music is turned off.")


# 4. MAIN USER INTERFACE
st.markdown('<div class="cozy-card">', unsafe_allow_html=True)

st.title("🌱 Cozy Productivity Center")

if user_motivation:
    st.markdown(f'<div class="motivation-banner">✨ "{user_motivation}"</div>', unsafe_allow_html=True)

st.markdown("Your peaceful environment for deep work. Choose your background sound below and tap into your workspace apps seamlessly.")
st.markdown("---")

# Main Hub Application Direct Launch Grid
st.subheader("🚀 Open Your Productivity Ecosystem")

# Grid layout with 3 columns
col_ypt, col_forest, col_pomo = st.columns(3)

with col_ypt:
    st.markdown("### 📺 Study With Me Stream")
    st.markdown("Watch an aesthetic, peaceful focus room video to study alongside.")
    st.video("https://www.youtube.com/watch?v=turbZg2m8I0")

with col_forest:
    st.markdown("### 🌲 Forest App")
    st.markdown("Stay focused, plant virtual seeds, and grow your digital woods.")
    st.markdown('<a href="https://www.forestapp.cc/" target="_blank" class="app-button">🌱 Open Forest</a>', unsafe_allow_html=True)

with col_pomo:
    st.markdown("### 🍅 Pomodoro")
    st.markdown("Work efficiently using customizable 25-minute focus intervals.")
    st.markdown('<a href="https://pomofocus.io/" target="_blank" class="app-button">⏳ Open Pomofocus</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
