import streamlit as st
from PIL import Image
import os
import time
from streamlit_extras.let_it_rain import rain

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Love Me ❤️",
    page_icon="❤️",
    layout="centered"
)

# ---------------- CLEAN RESPONSIVE CSS ----------------
st.markdown("""
<style>

body {
    background-color: white;
}

.block-container {
    padding-top: 2rem;
}

/* Responsive Title */
.main-title {
    font-size: clamp(28px, 6vw, 48px);
    text-align: center;
    font-weight: bold;
    color: #ff4d88;
    text-shadow: 0 0 12px #ff99cc;
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(45deg, #ff66a3, #ff1a75);
    color: white;
    font-size: clamp(16px, 4vw, 20px);
    border-radius: 30px;
    padding: 12px;
    border: none;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.05);
}

/* Text */
.responsive-text {
    font-size: clamp(18px, 5vw, 22px);
    text-align: center;
    color: #ff4d88;
    margin-top: 15px;
    min-height: 60px;
}

.final-text {
    font-size: clamp(26px, 6vw, 40px);
    text-align: center;
    color: #ff1a75;
    font-weight: bold;
    margin-top: 25px;
}

img {
    border-radius: 20px;
    max-width: 100%;
    height: auto;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# ---------------- LANDING PAGE ----------------
if not st.session_state.accepted:

    st.markdown('<div class="main-title">💖 Love Me - Valentine’s Special 💖</div>', unsafe_allow_html=True)
    st.markdown('<div class="responsive-text">Will you be my Valentine?</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes ❤️"):
            st.session_state.accepted = True

    with col2:
        if st.button("No 😏"):
            st.warning("No option disabled by destiny 😉")

# ---------------- LOVE REVEAL ----------------
else:

    # Floating animations
    rain(emoji="❤️", font_size=24, falling_speed=4, animation_length="infinite")
    rain(emoji="💋", font_size=20, falling_speed=3, animation_length="infinite")
    rain(emoji="🤗", font_size=22, falling_speed=4, animation_length="infinite")

    st.balloons()

    st.markdown('<div class="responsive-text">You unlocked my heart 💘</div>', unsafe_allow_html=True)

    image_folder = "pictures"

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

            img_placeholder.image(img, use_container_width=True)

            # Typewriter effect (stable)
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
        st.error("Images folder not found.")