import streamlit as st
from PIL import Image
import os
import time
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

# ---------------- LUXURY CSS ----------------
st.markdown("""
<style>

/* Soft romantic background */
body {
    background: radial-gradient(circle at center, #fff5f8 0%, #ffffff 65%);
}

/* Hide Streamlit footer */
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main Title */
.main-title {
    font-size: clamp(36px, 7vw, 54px);
    text-align: center;
    font-weight: 700;
    color: #ff3d7f;
    text-shadow: 0 0 25px rgba(255, 105, 180, 0.25);
    margin-top: 40px;
}

/* Subtitle */
.subtitle {
    font-size: clamp(20px, 5vw, 28px);
    text-align: center;
    color: #ff5c99;
    margin-top: 15px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #ff6fa5, #ff2e79);
    color: white;
    font-size: 20px;
    border-radius: 40px;
    padding: 14px 40px;
    border: none;
    box-shadow: 0 8px 20px rgba(255, 105, 180, 0.18);
    transition: transform 0.2s ease;
}

.stButton>button:hover {
    transform: translateY(-2px);
}

/* Message text */
.message-text {
    font-size: clamp(24px, 6vw, 34px);
    text-align: center;
    color: #ff4d88;
    margin-top: 25px;
    min-height: 90px;
    font-weight: 500;
    animation: fadeText 1.5s ease-in-out;
}

/* Final text */
.final-text {
    font-size: clamp(42px, 9vw, 70px);
    text-align: center;
    color: #ff2e79;
    font-weight: 700;
    margin-top: 60px;
    letter-spacing: 1px;
    animation: heartbeat 1.8s infinite;
}

/* Image cinematic zoom */
img {
    border-radius: 25px;
    animation: cinematicZoom 6s ease-in-out forwards;
    box-shadow: 0 20px 50px rgba(255, 105, 180, 0.18);
}

/* Animations */
@keyframes fadeText {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes heartbeat {
    0% { transform: scale(1); }
    50% { transform: scale(1.06); }
    100% { transform: scale(1); }
}

@keyframes cinematicZoom {
    0% { transform: scale(1); opacity: 0; }
    20% { opacity: 1; }
    100% { transform: scale(1.05); }
}

</style>
""", unsafe_allow_html=True)

# ---------------- LANDING PAGE ----------------
if not st.session_state.accepted:

    st.markdown('<div class="main-title">Do you Love Me? 💖</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Say yes na 🥺</div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    col_left, col_center, col_right = st.columns([1, 2, 1])

    with col_center:
        if st.button("Yes ❤️", use_container_width=True):
            st.session_state.accepted = True

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("No 😌", use_container_width=True):
            st.warning("Take your time… but I’ll still wait ❤️")

# ---------------- LOVE REVEAL ----------------
else:

    # Subtle floating heart
    rain(
        emoji="❤️",
        font_size=16,
        falling_speed=2.5,
        animation_length="infinite"
    )

    st.markdown('<div class="message-text">You unlocked my heart 💘</div>', unsafe_allow_html=True)

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

            displayed_text = ""
            for char in message:
                displayed_text += char
                text_placeholder.markdown(
                    f"<div class='message-text'>{displayed_text}</div>",
                    unsafe_allow_html=True
                )
                time.sleep(0.035)

            time.sleep(2.5)

        st.markdown('<div class="final-text">I Love You ❤️</div>', unsafe_allow_html=True)

    else:
        st.error("Pictures folder not found.")
