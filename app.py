import streamlit as st
from PIL import Image
import os
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="For You ❤️",
    page_icon="❤️",
    layout="centered"
)

# ---------------- CINEMATIC CSS ----------------
st.markdown("""
<style>

/* Soft luxury background */
body {
    background: linear-gradient(180deg, #fff8fb 0%, #ffffff 100%);
}

/* Hide Streamlit header/footer */
header {visibility: hidden;}
footer {visibility: hidden;}

/* Main message text */
.message-text {
    font-size: clamp(28px, 6vw, 40px);
    text-align: center;
    color: #ff3d7f;
    margin-top: 50px;
    min-height: 120px;
    font-weight: 500;
}

/* Final love text */
.final-text {
    font-size: clamp(50px, 10vw, 90px);
    text-align: center;
    color: #ff1a66;
    font-weight: 700;
    margin-top: 120px;
    animation: heartbeat 1.6s infinite;
}

/* Heartbeat animation */
@keyframes heartbeat {
    0% { transform: scale(1); }
    25% { transform: scale(1.05); }
    40% { transform: scale(1); }
    60% { transform: scale(1.08); }
    100% { transform: scale(1); }
}

/* Smooth fade image */
img {
    border-radius: 30px;
    animation: fadeInImage 1.5s ease-in-out;
    box-shadow: 0 25px 60px rgba(255, 105, 180, 0.2);
}

@keyframes fadeInImage {
    from { opacity: 0; transform: scale(0.97); }
    to { opacity: 1; transform: scale(1); }
}

</style>
""", unsafe_allow_html=True)

# ---------------- OPTIONAL BACKGROUND MUSIC ----------------
if os.path.exists("romantic.mp3"):
    st.audio("romantic.mp3", autoplay=True)

# ---------------- SLIDESHOW ----------------
image_folder = "pictures"

if os.path.exists(image_folder):

    images = sorted(os.listdir(image_folder))

    messages = [
        "I wanna love you again…",
        "Not from where we began.",
        "But from where we paused.",
        "Not with fear…",
        "But with understanding.",
        "Not with expectations…",
        "But with patience.",
        "Between silence and memories…",
        "I still find you.",
        "Even after everything…",
        "My heart never really left.",
        "So here I am…",
        "Choosing you again."
    ]

    img_placeholder = st.empty()
    text_placeholder = st.empty()

    for i in range(len(images)):

        img_path = os.path.join(image_folder, images[i])
        img = Image.open(img_path)

        img_placeholder.image(img, use_container_width=True)

        message = messages[i % len(messages)]

        displayed = ""
        for char in message:
            displayed += char
            text_placeholder.markdown(
                f"<div class='message-text'>{displayed}</div>",
                unsafe_allow_html=True
            )
            time.sleep(0.04)

        time.sleep(2.5)

    st.markdown('<div class="final-text">I Love You ❤️</div>', unsafe_allow_html=True)

else:
    st.error("Pictures folder not found.")
