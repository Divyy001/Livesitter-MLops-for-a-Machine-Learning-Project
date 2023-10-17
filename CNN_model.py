from PIL import Image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array, ImageDataGenerator
from tensorflow.keras.models import Model




def feature_extraction(image):
    # load vgg16 model
    model = VGG16()
    # restructure the model
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)

    features = {}
    image = Image.fromarray(image)
    image = image.resize((224, 224), Image.BILINEAR) 
    # convert image pixels to numpy array
    image = img_to_array(image)
    # reshape data for model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # preprocess image for vgg
    image = preprocess_input(image)
    # extract features
    feature = model.predict(image, verbose=0)

    return feature

        