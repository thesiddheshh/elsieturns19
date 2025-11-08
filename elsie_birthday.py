import streamlit as st

# -------------------------------
# 🎀 EDITABLE CONTENT SECTION
# -------------------------------
ELSI_MESSAGE = """
five whole years. like, how did that even happen? sometimes it still blows my mind that someone i met online has become my person. there hasn’t been a single thing that’s happened — good, bad, stupid, or completely random — where my first instinct wasn’t “i gotta tell elsie.” you’ve become that one constant in my life, the one i can always run to, no matter what time it is or how i’m feeling.

you’ve seen me at my happiest and my absolute lowest, and somehow you’ve stayed through it all. and i love that about you. i love how you’re always so open with me, how you tell me about your days — the good, the bad, the “i just wanna disappear” ones — and how it never feels forced. it’s just us, being real with each other. i don’t think you even realize how much that means to me.

sometimes i wish i could just show up at your door with a handwritten letter and a big bouquet, and maybe a little gift that makes you laugh because it’s so us. but we live exactly 5704 kms apart, which is honestly rude of the universe. i’d give anything to just be there today, to see you smile in person and annoy you until you tell me to shut up.

but one day we’re gonna meet, and when that happens, i’m hugging you so tight you’ll need to call an ambulance (out of love obviously). until then, please take care of yourself, eat an unreasonable amount of cake, do something that makes you happy, and remember — i’m so damn proud of the person you are.

happy birthday, elsie. my favorite human on the other side of the world, my comfort person, and ofc my pookie. 💕

love, siddh.
"""

# ✅ Clean Spotify embed URL (no spaces!)
SPOTIFY_PLAYLIST_EMBED_URL = "https://open.spotify.com/embed/playlist/6gi54nFBG8CUb0MNdU6tmt"

# ✅ Your custom images from GitHub (upload to: /images/photo1.jpg, etc.)
BASE_IMG = "https://raw.githubusercontent.com/thesiddheshh/elsieturns19/main/images"
PHOTO_URLS = [
    f"{BASE_IMG}/photo1.jpg",
    f"{BASE_IMG}/photo2.jpg",
    f"{BASE_IMG}/photo3.jpg",
    f"{BASE_IMG}/photo4.jpg",
    f"{BASE_IMG}/photo5.jpg",
    f"{BASE_IMG}/photo6.jpg",
]

# -------------------------------

# Hide Streamlit UI
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Custom Birthday CSS (cleaned: no section cards for music/photos)
birthday_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;500&family=Homemade+Apple&display=swap');

    .stApp {
        background: linear-gradient(135deg, #fbeaf2 0%, #e5f6ff 100%);
        font-family: 'Poppins', sans-serif;
        padding: 0;
        margin: 0;
    }

    .main-content {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem 1.5rem;
    }

    .elsie-title {
        font-family: 'Dancing Script', cursive;
        font-size: 4.2rem;
        color: #7a5f8c;
        text-align: center;
        margin-bottom: 1.8rem;
        text-shadow: 0 2px 6px rgba(0,0,0,0.08);
        animation: fadeIn 1.2s ease-out;
    }

    .message-card {
        background: url('https://www.toptal.com/designers/subtlepatterns/patterns/letter-paper.png'), #fff9f5;
        background-size: 150px;
        border-radius: 12px;
        padding: 2.4rem;
        margin-bottom: 2.2rem;
        box-shadow: 0 8px 24px rgba(160, 130, 190, 0.25);
        font-family: 'Homemade Apple', cursive;
        font-size: 1.35rem;
        line-height: 1.8;
        color: #5a4a66;
        position: relative;
        animation: floatIn 1s ease-out;
        text-align: left;
        border: 1px solid #f7e9f1;
    }

    .section-title {
        font-family: 'Dancing Script', cursive;
        font-size: 2.4rem;
        color: #8a6d9d;
        text-align: center;
        margin: 1.8rem 0 1.2rem;
    }

    .photo-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
        gap: 16px;
        margin-top: 0.8rem;
    }

    .photo-item {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        aspect-ratio: 1 / 1;
    }

    .photo-item:hover {
        transform: scale(1.06);
    }

    .photo-item img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border: 3px solid #fff;
        border-radius: 16px;
    }

    .spotify-embed {
        display: flex;
        justify-content: center;
        margin: 1.2rem 0;
    }

    .decoration {
        position: fixed;
        z-index: -1;
        opacity: 0.6;
    }

    .heart-1 { top: 10%; left: 5%; font-size: 24px; color: #e0b3d0; animation: float 8s ease-in-out infinite; }
    .heart-2 { top: 70%; right: 8%; font-size: 18px; color: #b3e0d1; animation: float 10s ease-in-out infinite reverse; }
    .star-1 { top: 20%; right: 12%; font-size: 14px; color: #c7b3e0; animation: twinkle 4s infinite; }
    .star-2 { bottom: 15%; left: 10%; font-size: 16px; color: #d0b3e0; animation: twinkle 5s infinite 1s; }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes floatIn {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }

    @keyframes twinkle {
        0%, 100% { opacity: 0.4; }
        50% { opacity: 1; }
    }

    @media (max-width: 600px) {
        .elsie-title { font-size: 3.2rem; }
        .message-card { padding: 1.6rem; font-size: 1.2rem; }
        .section-title { font-size: 2rem; }
        .photo-grid { grid-template-columns: repeat(2, 1fr); gap: 12px; }
    }
</style>

<!-- Decorative elements -->
<div class="decoration heart-1">♥</div>
<div class="decoration heart-2">♥</div>
<div class="decoration star-1">✧</div>
<div class="decoration star-2">✧</div>
"""

st.markdown(birthday_css, unsafe_allow_html=True)

# -------------------------------
# 🎂 MAIN LAYOUT
# -------------------------------
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown('<div class="elsie-title">Happy Birthday, Elsie!</div>', unsafe_allow_html=True)

# Letter
st.markdown(f'<div class="message-card">{ELSI_MESSAGE}</div>', unsafe_allow_html=True)

# Music
st.markdown('<div class="section-title">lil playlist to make your day </div>', unsafe_allow_html=True)
st.markdown(f'''
<div class="spotify-embed">
    <iframe style="border-radius:12px" src="{SPOTIFY_PLAYLIST_EMBED_URL}" 
    width="100%" height="152" frameBorder="0" allow="clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
</div>
''', unsafe_allow_html=True)

# Photos
st.markdown('<div class="section-title">memories with you </div>', unsafe_allow_html=True)
st.markdown('<div class="photo-grid">', unsafe_allow_html=True)
for url in PHOTO_URLS:
    st.markdown(f'<div class="photo-item"><img src="{url}" alt="Elsie"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
