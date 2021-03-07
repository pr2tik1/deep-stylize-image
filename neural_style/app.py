import streamlit as st 
from PIL import Image 
import style 

im = Image.open('banner.jpg')
st.image(im)

st.write("Stylize your Image from the available styles. Just choose from the options in the sidebar and click '**stylize**'. \
    This app uses style transfer deep learning technique. To know more follow the model training and code visit \
        [here](https://github.com/pytorch/examples/tree/master/fast_neural_style). **Note** first run image and style from \
            sidebar, then upload your own image.")

img = st.sidebar.selectbox(
    "Select Image",
    ("amber.jpg","dog.jpg","author.png","cat.jpg","flower.jpg")
)

style_name = st.sidebar.selectbox(
    "Select Style",
    ('candy','mosaic','udnie','rain_princess')
)

model = "saved_models/" + style_name + ".pth"
input_image = "images/content-images/" + img  
output_image = "images/output-images/" + style_name + "-" + img 

image_uploaded = st.file_uploader("Upload an image: ", type="jpg")

if image_uploaded is not None:
    input_ = image_uploaded
    image = Image.open(image_uploaded)
else:
    input_ = input_image
    image = Image.open(input_image)

st.write("### Source Image: ")
st.image(image, use_column_width='always')

clicked = st.button("Stylize")
if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)

    st.write("### Output Image")
    image = Image.open(output_image)
    st.image(image, use_column_width='always')

st.write("What a style!")