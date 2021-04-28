import os
import streamlit as st 
from PIL import Image 
import style 
import time 

#Main Title
im = Image.open('banner.jpg')
st.image(im)

#Style images 
st.write("## 🤩 Style Images \
        \nFollowing are the style images can be used. Choose from the sidebar options.")
im_1 = Image.open("images/style-images/candy.jpg")
im_2 = Image.open("images/style-images/mosaic.jpg")
im_3 = Image.open("images/style-images/rain-princess.jpg")
im_4 = Image.open("images/style-images/udnie.jpg")
col1, col2, col3, col4  = st.beta_columns(4)
with col1:
    st.image(im_1, width=100)
    st.write("Candy")
with col2:
    st.image(im_2, width=120)
    st.write("Mosaic")
with col3:
    st.image(im_3, width=100)
    st.write("Rain Princess")
with col4:
    st.image(im_4, width=100)
    st.write("Udnie")

st.write("## 📲Content Image \
        \nUpload your content image from below option of 'Browse Files'.")

#Sidebar
st.sidebar.title("Deep Stylize Image")
st.sidebar.write("Steps: \
    \n1. Upload via 'Browse Files'\
    \n2. Choose a style and click 'Stylize' \
    \n3. Breathe and let model work")
#Style options
style_name = st.sidebar.selectbox(
    "Style Options",
    ('candy','mosaic','udnie','rain_princess')
)

#Default value and Uploading images
img = st.sidebar.selectbox(
    'Select Image',('cat', 'catface', 'sunset', 'banana'), 
)

image_uploaded = st.file_uploader("(Image size must below 200kB so that you don't kill the app!)", type="jpg")

#Loading model
model = "saved_models/" + style_name + ".pth"
input_image = "images/content-images/" + img  + ".jpg"


#If no image is uploaded set default image as amber
if image_uploaded is None:
    input_ = input_image
    image = Image.open(input_image)
else:
    image = Image.open(image_uploaded)
    img = str(image_uploaded)
    image.save("images/compressed-images/compressed_"+ img +".jpg", optimize = True, quality=30)#Change quality using 
    compressed_image  ="images/compressed-images/compressed_"+ img +".jpg"
    input_ = compressed_image

#Output images path
output_image = "images/output-images/" + style_name + "-" + img + ".jpg"

st.write("## 👨‍💻 Let's deep stylize \
        \n In this segment left side we have uploaded image which is our content image\
        and right side we have output image. To save output image, just right click and choose 'Save Image as' option.")

#Columns for input and output images
col1, col2 = st.beta_columns(2)
with col1:
    st.write("### 🖼Source Image: ")
    if image_uploaded is None:
        st.image(image, use_column_width='always')
    else:
        st.image(compressed_image, use_column_width='always')

#Stylize the input image
st.sidebar.write("😎 **Run styling** ",)
clicked = st.sidebar.button("Stylize")
if clicked:
    
    model = style.load_model(model)
    style.stylize(model, input_, output_image)
    
    
    with col2:
        st.write("### 🎉Output Image")
        image = Image.open(output_image)
        st.image(image, use_column_width='always')

    st.success('Done! 🚀')
    st.balloons()

st.sidebar.write('**Note:** Please use small size images(<200kB). \
    \n**Why?** \
    \nBecause there are [limitations](https://stackoverflow.com/a/66586602/15377016) to something free.')
st.sidebar.write("*Made by Pratik Kumar*")
st.write('To know more about the application development and code follow [here](https://github.com/pr2tik1/deep-stylize-image).')
