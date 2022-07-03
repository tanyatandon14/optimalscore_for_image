from email.mime import image
import streamlit as st 
from PIL import Image 
import time 
import random

def load_image(image_file):
    img = Image.open(image_file)
    return img
rad= st.sidebar.radio("navigation",["Home","About Us "])  
st.title("Welcome to Compressor I\O")
if rad== "Home":
    image_file = st.file_uploader("Upload Images you want to compress", type=["png","jpg","jpeg"])
    if image_file is not None:
        st.image(load_image(image_file),width=250)
        st.success("image successfully uploaded ") 
        st.write("original size of the image:") 
        file_details= image_file.size 
        st.write(file_details)
        
    if st.button("find compression ratio") :
        progress= st.progress(0)
        for i in range(100): 
            time.sleep(0.01)
            progress.progress(i+1)
        st.info("optimal score for compression:") 
        
        st.info((score.py)) # will return the score from the score.py script of the function 
 
if rad =="About Us":
      st.heading("ABOUT US ")
      st.write("compressorI/O is aimed to solve the problem to solve various size  and resolution of image in the cloud which is costly and aldo results in longer upload time and higher space utilization in the cloud so compressorI/O provides the optimal score range 0 to 100 of pixel density for an imageto which the input image can be dropped to , while preserving the most of the image quality ")
#st.image("project//compressed.jpg")


