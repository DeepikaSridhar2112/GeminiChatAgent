import streamlit as st
import time
from dotenv import find_dotenv, load_dotenv
from utils import generate_response, get_llm
from PIL import Image
import tempfile



load_dotenv(find_dotenv(),override=True)
st.title("Interactive chat with Gemini Clone:heart:")
st.set_page_config(page_title="Interactive chat with Gemini Clone", page_icon=":robot_face:")

import streamlit as st

st.markdown("""
    <style>
    div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 18px;
        color: grey;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

model = get_llm()
chat = model.start_chat(history=())
choice = st.radio(
    "Choose a option to work with:",
    ("Text", "Image", "Audio","Leave Chat Room"),
    index=0
)

if choice == "Text":
   prompt= st.text_area("enter your text")
   submit=st.button('submit')
   if submit:
     st.write(generate_response(model,choice,query=prompt))
elif choice == "Image":
   uploaded_file = st.file_uploader("Upload any image", type=["png", "jpg", "jpeg"])
   upload = st.button('submit')
   if(upload):
     if uploaded_file is not None:
       image = Image.open(uploaded_file)
       st.write(generate_response(model,choice,image=image))
     else:
          st.warning("Please upload an image file.")
elif choice == "Audio":
   uploaded_file = st.file_uploader("Upload any audio file", type=["mp3"])
   upload = st.button('submit')
   if(upload):
     if uploaded_file is not None:
       with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as uploadedAudio:
         uploadedAudio.write(uploaded_file.read())
         file_path = uploadedAudio.name
         st.write(generate_response(model,choice,audio_file=file_path))
     else:
          st.warning("Please upload an audio file.")
else:
     st.info("Come back soon! ❄️")
     st.snow()
