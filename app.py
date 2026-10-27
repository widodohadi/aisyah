from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Untuk Kamu, Cintaku", page_icon="💗", layout="centered")

# Sembunyikan menu, header, dan footer bawaan Streamlit agar tampil seperti halaman biasa
st.markdown(
    """
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "romantis.html").read_text(encoding="utf-8")
components.html(html, height=1500, scrolling=True)
