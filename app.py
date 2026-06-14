import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="HopDrop — Shared Delivery Prototype",
    page_icon="📦",
    layout="wide",
)

# Hide Streamlit's default chrome so the prototype takes over the page
st.markdown(
    """
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; }
        header, footer { visibility: hidden; height: 0; }
        iframe { display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "hopdrop.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=900, scrolling=True)
