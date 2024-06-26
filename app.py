import os
import json
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase desde las credenciales JSON
cred_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', 'ayemood5-firebase-adminsdk-50x2w-31174e8b65.json')
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

# Inicializar Firestore
db = firestore.client()

# Función para obtener el emoji actual desde Firestore
def get_current_emoji():
    doc_ref = db.collection('emojis').document('current_emoji')
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict().get('emoji', '😀')
    else:
        return '😀'

# Función para actualizar el emoji en Firestore
def update_emoji(new_emoji):
    doc_ref = db.collection('emojis').document('current_emoji')
    doc_ref.set({'emoji': new_emoji})

# Leer el emoji actual desde Firestore
emoji = get_current_emoji()

st.title("AYEMOOD")
st.markdown(f"<div style='text-align: center; font-size: 100px;'>{emoji}</div>", unsafe_allow_html=True)

# Entrada para actualizar el emoji
new_emoji = st.text_input("Introduce un emoji:", value=emoji)

if st.button("ACTUALIZAR"):
    update_emoji(new_emoji)
    st.markdown(f"<div style='text-align: center; font-size: 100px;'>{new_emoji}</div>", unsafe_allow_html=True)

# Ocultar la marca de agua de Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)