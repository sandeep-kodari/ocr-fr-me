import streamlit as st 
import pytesseract 
from PIL import Image 
pytesseract.pytesseract.tesseract_cmd='/app/.apt/usr/bin/tesseract' 
st.title("OCR-optical character recognition") 
img=st.file_uploader("choose an image") 
if image is not None: 
  img_read=Image.open(img) 
  st.image(img,caption='uploaded image') 
  if st.button('predict'): 
    op=pytesseract.image_to_string(img_read) 
    st.write(op)
