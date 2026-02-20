import streamlit as st
from PIL import Image
import os
import time
import random
from streamlit_extras.let_it_rain import rain

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Do you Love Me? ❤️",
    page_icon="❤️",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "accepted" not in st.session_state:
    st.session_state.accepted = False

if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

# ---------------- CLEAN CSS ----------------
st.markdown("""
<style>
body {
    background-color: white;
}

.main-title {
    font-size: clamp(32px, 6vw, 50px);
    text-align: center;
    font-weight: bold;
    color: #ff4d88;
    text-shadow: 0 0 12px #ff99cc;
}

.responsive-text {
    font-size: clamp(24px, 6vw, 34px);
    text-align: center;
    color: #ff4d88;
    margin-top: 20px;
    min-height: 80px;
    font-weight: 500;
}

.final-text {
    font-size: clamp(36px, 8vw, 60px);
    text-align: center;
    color: #ff1a75;
    font-weight: bold;
    margin-top: 35px;
}

.stButton>button {
    background: linear-gradient(45deg, #ff66a3, #ff1a75);
    color: white;
    font-size: 20px;
    border-radius: 30px;
    padding: 12px 30px;
    border: none;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.1);
}

img {
    border-radius: 20px;
    max-width: 100%;
    height: auto;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LANDING PAGE ----------------
if not st.session_state.accepted:

    st.markdown('<div class="main-title"> Do you Love Me? 💖</div>', unsafe_allow_html=True)
    st.markdown('<div class="responsive-text">Say yes na 🥺</div>', unsafe_allow_html=True)

    # 5 columns so Yes stays centered
    cols = st.columns(5)

    yes_position = 2
    no_position = random.randint(0, 4) if st.session_state.no_clicks > 0 else 3

    with cols[yes_position]:
        if st.button("Yes ❤️"):
            st.session_state.accepted = True

    with cols[no_position]:
        if st.button("No 😏"):
            st.session_state.no_clicks += 1
            st.rerun()

# ---------------- LOVE REVEAL ----------------
else:

    # Soft floating emoji (single layer)
    rain(
        emoji=random.choice(["❤️", "💋"]),
        font_size=16,
        falling_speed=3,
        animation_length="infinite"
    )

    st.markdown('<div class="responsive-text">You unlocked my heart 💘</div>', unsafe_allow_html=True)

    image_folder = "pictures"   # Make sure this folder exists

    if os.path.exists(image_folder):

        images = sorted(os.listdir(image_folder))

        messages = [
            "I wanna love you again… not from where we began, but from where we paused.",
            "Not with fear… but with understanding.",
            "Not with expectations… but with patience.",
            "Between silence and memories… I still find you.",
            "Even after everything… my heart never really left.",
            "So here I am… choosing you again."
        ]

        img_placeholder = st.empty()
        text_placeholder = st.empty()

        for img_file, message in zip(images, messages):

            img_path = os.path.join(image_folder, img_file)
            img = Image.open(img_path)

            # SIMPLE image display (no HTML wrapper)
            img_placeholder.image(img, use_container_width=True)

            # Typewriter text
            displayed_text = ""
            for char in message:
                displayed_text += char
                text_placeholder.markdown(
                    f"<div class='responsive-text'>{displayed_text}</div>",
                    unsafe_allow_html=True
                )
                time.sleep(0.03)

            time.sleep(2)

        st.markdown('<div class="final-text">I Love You ❤️</div>', unsafe_allow_html=True)
        st.markdown('<div class="responsive-text">This time… let’s not lose us.</div>', unsafe_allow_html=True)

    else:
        st.error("Pictures folder not found.")
