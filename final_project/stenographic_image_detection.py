from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

def detect_steganographic_image(image_path, model_path):
    model = load_model(model_path)
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    if prediction[0] > 0.5:
        print("The image is steganographic.")
    else:
        print("The image is normal.")

detect_steganographic_image('path/to/received/image.jpg', 'path/to/fine_tuned_model.h5')
