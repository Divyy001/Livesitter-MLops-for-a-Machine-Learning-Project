import streamlit as st
import numpy as np
from tqdm.notebook import tqdm
import cv2
from CNN_model import feature_extraction
from keras.models import load_model 
from predict_caption import predict_caption
from tensorflow.keras.preprocessing.text import Tokenizer

max_length = 35

## fitting the caption data 
## initializing the tokenizer

with open('captions.txt', 'r') as f:
    next(f)
    captions_doc = f.read()

# create mapping of image to captions
mapping = {}
# process lines
for line in tqdm(captions_doc.split('\n')):
    # split the line by comma(,)
    tokens = line.split(',')
    if len(line) < 2:
        continue
    image_id, caption = tokens[0], tokens[1:]
    # remove extension from image ID
    image_id = image_id.split('.')[0]
    # convert caption list to string
    caption = " ".join(caption)
    # create list if needed
    if image_id not in mapping:
        mapping[image_id] = []
    # store the caption
    mapping[image_id].append(caption)

def clean(mapping):
    for key, captions in mapping.items():
        for i in range(len(captions)):
            # take one caption at a time
            caption = captions[i]
            # preprocessing steps
            # convert to lowercase
            caption = caption.lower()
            # delete digits, special chars, etc., 
            caption = caption.replace('[^A-Za-z]', '')
            # delete additional spaces
            caption = caption.replace('\s+', ' ')
            # add start and end tags to the caption
            caption = 'startseq ' + " ".join([word for word in caption.split() if len(word)>1]) + ' endseq'
            captions[i] = caption


clean(mapping)

all_Captions = []
for key in mapping:
    for caption in mapping[key]:
        all_Captions.append(caption)


# tokenize the text
tokenizer = Tokenizer()
tokenizer.fit_on_texts(all_Captions)
vocab_size = len(tokenizer.word_index) + 1

# Load model configuration

loaded_model = load_model("network1.h5", compile=False) 
# loss, accuracy = loaded_model.evaluate(test_data, test_targets) 
loaded_model.compile(loss='categorical_crossentropy', optimizer='adam')

# UI Components
st.title("Image Captioning Model")

st.write("Upload your image and Generate Caption automatically")

image = st.file_uploader("Insert Image")

if image is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)



if st.button("Generate Caption"):
    if opencv_image is None:
        st.write("Insert image to generate Caption")
        
    else:
        features = feature_extraction(opencv_image)
        # tokenizer = Tokenizer()
        prediction = predict_caption(loaded_model, features, tokenizer, max_length)
        # prediction = prediction.strip(".").strip()
        st.write(prediction)