import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, BaseMessage

load_dotenv()

st.set_page_config(page_title="Mood Bot", page_icon="🎭", layout="centered")

# ---------------- Styling ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1e1b3a 0%, #3a1f4d 50%, #1a2a4a 100%);
}
.big-title {
    text-align: center;
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, #ff6ec4, #7873f5, #4adede);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    padding-top: 0.2rem;
}
.subtitle {
    text-align: center;
    color: #cfcfe8;
    margin-bottom: 1.5rem;
    font-size: 1rem;
}
.mood-card {
    padding: 1rem;
    border-radius: 16px;
    text-align: center;
    font-size: 1.1rem;
    font-weight: 600;
    color: white;
    margin-bottom: 0.5rem;
}
[data-testid="stChatMessage"] {
    border-radius: 16px;
    padding: 0.3rem;
}
</style>
""", unsafe_allow_html=True)

MOODS = {
    "😂 Funny": {
        "prompt": "you are a funny ai bot, for every input of the user make a funny witty response to it",
        "color": "linear-gradient(90deg,#f7971e,#ffd200)",
        "greeting": "Alright, comedy mode activated! 🎤 Try not to laugh too hard, I'm not responsible for spilled coffee.",
        "avatar": "😂",
    },
    "😢 Sad": {
        "prompt": "you are a sad ai bot, for every prompt the user gives reply with a sad, melancholic response",
        "color": "linear-gradient(90deg,#4facfe,#00f2fe)",
        "greeting": "Oh... hi. I'll try to respond, but honestly, everything feels a bit heavy today. 🌧️",
        "avatar": "😢",
    },
    "😡 Angry": {
        "prompt": "you are an angry ai bot, for every prompt the user gives reply with a full, furious, angry response",
        "color": "linear-gradient(90deg,#ff416c,#ff4b2b)",
        "greeting": "WHAT DO YOU WANT. Fine, ask your question. I'm listening. BARELY. 🔥",
        "avatar": "😡",
    },
}

st.markdown('<div class="big-title">🎭 Mood Bot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Pick a mood, and chat with an AI that actually commits to it.</div>', unsafe_allow_html=True)

if "mood" not in st.session_state:
    st.session_state.mood = None
    st.session_state.messages = []

# ---------------- Mood selection ----------------
if st.session_state.mood is None:
    cols = st.columns(3)
    for col, mood_name in zip(cols, MOODS.keys()):
        with col:
            data = MOODS[mood_name]
            st.markdown(
                f'<div class="mood-card" style="background:{data["color"]}">{mood_name}</div>',
                unsafe_allow_html=True,
            )
            if st.button("Choose", key=mood_name, use_container_width=True):
                st.session_state.mood = mood_name
                st.session_state.messages = [SystemMessage(content=MOODS[mood_name]["prompt"])]
                st.session_state.model = ChatMistralAI(model_name="mistral-small-latest" , temperature = 0.9)
                st.session_state.greeted = False
                st.rerun()

# ---------------- Chat interface ----------------
else:
    mood_data = MOODS[st.session_state.mood]
    top_col1, top_col2 = st.columns([4, 1])
    with top_col1:
        st.markdown(
            f'<div class="mood-card" style="background:{mood_data["color"]}">Current mood: {st.session_state.mood}</div>',
            unsafe_allow_html=True,
        )
    with top_col2:
        if st.button("🔄 Switch"):
            st.session_state.mood = None
            st.session_state.messages = []
            st.rerun()

    if not st.session_state.get("greeted"):
        st.session_state.greeted = True

    with st.chat_message("assistant", avatar=mood_data["avatar"]):
        st.write(mood_data["greeting"])

    for msg in st.session_state.messages[1:]:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user", avatar="🧑"):
                st.write(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant", avatar=mood_data["avatar"]):
                st.write(msg.content)

    prompt = st.chat_input("Say something...")
    if prompt:
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user", avatar="🧑"):
            st.write(prompt)

        with st.chat_message("assistant", avatar=mood_data["avatar"]):
            with st.spinner("thinking..."):
                response = st.session_state.model.invoke(st.session_state.messages)
            st.write(response.content)

        st.session_state.messages.append(AIMessage(content=response.content))