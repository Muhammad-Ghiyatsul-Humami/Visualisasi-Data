import streamlit as st


st.title("Data and Media Elements")
st.markdown("**Kelompok 15**")
st.markdown("""
1. Abdu Azzam Alaris - 0110122073
2. M. Ghiyatsul Humami - 0110220108
3. Nurul Aeman - 0110222099
            """)

("---------------------------------------------------------------------")

st.subheader ("Images")

st.write("Display an Images")

#display image by specifying path

st.image("Aset/hopper_1.jpg")


st.write("Image Courtesy: unplash.com") #image courtesy by unplash

("--------------------------------------------------------------------------")

#image courtesy
st.write("Display Multiple Images")

#listing out animal images
animal_images = [
    
    'Aset/buffa.jpg',
    'Aset/hopper_1.jpg',
    'Aset/kivat.jpg',
    'Aset/naga.jpg',
    
]

#display multiple images with width 150
st.image(animal_images, width=150)

#image courtesy
st.write("Image Courtesy: Unplash")

("------------------------------------------------")

st.title("Background Image")

import base64

#function to set image as background
def add_local_background_image_(image) :
    with open(image, "rb") as image :
        encoded_string = base64.b64encode(image.read())
    st.write("Image Courtesy: unplash")
    st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url(data:files/{"jpg"}; base64, {encoded_string.decode()});
        background-size: cover
        }}
        </style>
        """,
    unsave_allow_html= True
    )

    st.write("Background Image")

    #calling Image in Function
    add_local_background_image_('Aset/buffa.jpg')

("--------------------------------")
import streamlit as st
from PIL import Image

original_image = Image.open("Aset/hopper_1.jpg")
#display original image

st.subheader("Original Image")
st.image(original_image)

#resizing image to 600*400
resized_image = original_image.resize((600, 400))

#display resized image
st.title("Resized Image")
st.image(resized_image)