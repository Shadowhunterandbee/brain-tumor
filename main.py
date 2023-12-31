import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np

from util import classify, set_background


set_background('/home/shambhavi/Downloads/archive(1)/doc.jpeg')

# set title
st.title('brain tumor classification')

# set header
st.header('Please upload an image')

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('/home/shambhavi/Downloads/archive(1)/tumor_model1.h5')

# Load class names
with open('/home/shambhavi/Downloads/archive(1)/labels.txt', 'r') as f:
    class_names = [line.strip().split(' ')[1] for line in f.readlines()]
    f.close()

# display image
# Display image and classification result
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name = classify(image, model, class_names, threshold=0.5)

#     # Display classification result
    st.write("## Classification Result:")
    st.write("### Class: {}".format(class_name))
#     # st.write("### Score: {:.2f}%".format(conf_score * 100))
# # st.write("### Score: {:.2f}%".format(conf_score[0] * 100))
