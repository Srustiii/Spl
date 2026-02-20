import streamlit as st
from PIL import Image
import os
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Do you Love Me? ❤️",
    page_icon="❤️",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "accepted" not in st.session_state:
    st.session_state.accepted = False

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

/* Title */
.main-title {
    font-size: clamp(40px, 8vw, 64px);
    text-align: center;
    font-weight: 700;
    color: #ff2e79;
    letter-spacing: 1px;
    margin-top: 60px;
}

/* Subtitle */
.subtitle {
    font-size: clamp(20px, 5vw, 28px);
    text-align: center;
    color: #ff6fa5;
    margin-top: 20px;
}

/* Buttons (NO SHADOW, NO GLOW) */
.stButton>button {
    background: linear-gradient(135deg, #ff7eb3, #ff2e79);
    color: white;
    font-size: 22px;
    border-radius: 50px;
    padding: 16px 40px;
    border: none;
    box-shadow: none;
    outline: none;
    transition: transform 0.2s ease;
}

.stButton>button:hover {
    transform: translateY(-2px);
}

/* Remove focus & active effects */
.stButton>button:focus,
.stButton>button:active {
    outline: none !important;
    box-shadow: none !important;
}

/* Message text */
.message-text {
    font-size: clamp(26px, 6vw, 38px);
    text-align: center;
    color: #ff3d7f;
    margin-top: 40px;
    min-height: 110px;
    font-weight: 500;
}

/* Final love text with heartbeat */
.final-text {
    font-size: clamp(50px, 10vw, 90px);
    text-align: center;
    color: #ff1a66;
    font-weight: 700;
    margin-top: 100px;
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
    box-shadow: 0 25px 60px rgba(255, 105, 180, 0.15);
}

@keyframes fadeInImage {
    from { opacity: 0; transform: scale(0.97); }
    to { opacity: 1; transform: scale(1); }
}

</style>
""", unsafe_allow_html=True)

# ---------------- LANDING PAGE ----------------
if not st.session_state.accepted:

    st.markdown('<div class="main-title">Do you Love Me? 💖</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">This time… say it softly.</div>', unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    col_left, col_center, col_right = st.columns([1, 2, 1])

    with col_center:
        if st.button("Yes ❤️", use_container_width=True):
            st.session_state.accepted = True
            st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("No 😌", use_container_width=True):
            st.warning("Take your time… I’m not going anywhere.")

# ---------------- LOVE REVEAL ----------------
else:


    st.markdown('<div class="message-text">You unlocked my heart 💘</div>', unsafe_allow_html=True)

    image_folder = "pictures"

    if os.path.exists(image_folder):

        images = sorted(os.listdir(image_folder))

        messages = [
            "I wanna love you again… not from where we began.",
            "But from where we paused.",
            "Not with fear…",
            "But with understanding.",
            "Not with expectations…",
            "But with patience.",
            "Between silence and memories…",
            "I still find you.",
            "And even after everything…",
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
                time.sleep(0.035)

            time.sleep(2.2)

        st.markdown('<div class="final-text">I Love You ❤️</div>', unsafe_allow_html=True)

    else:
        st.error("Pictures folder not found.")
