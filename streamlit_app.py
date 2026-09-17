import base64
import gzip
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title='MBA · Desafío SOBACIR 2026',
    layout='wide',
    initial_sidebar_state='collapsed',
)

st.markdown(
    """
    <style>
      [data-testid="stHeader"], [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"],
      footer { display: none !important; }
      html, body, [data-testid="stAppViewContainer"], .stApp {
        margin: 0 !important;
        padding: 0 !important;
        background: #fff !important;
      }
      [data-testid="stMain"] { padding: 0 !important; }
      .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      iframe { display: block; border: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

@st.cache_data(show_spinner=False)
def load_game() -> str:
    payload_dir = Path(__file__).parent / 'app_payload'
    encoded = ''.join(
        part.read_text(encoding='ascii')
        for part in sorted(payload_dir.glob('part*.txt'))
    )
    return gzip.decompress(base64.b64decode(encoded)).decode('utf-8')

components.html(load_game(), height=980, scrolling=False)
