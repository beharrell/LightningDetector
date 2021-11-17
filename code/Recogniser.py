import tensorflow.keras
import numpy as np
from PIL import ImageOps, Image

class Recogniser:
    def __init__(self):
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)
        print("Opening model")
        self.model = tensorflow.keras.models.load_model("..\\converted_keras\\keras_model.h5")
        print("Opened model")
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    def ContainsLightning(self, imageBig):
        size = (224, 224)
        image = ImageOps.fit(imageBig, size, Image.ANTIALIAS)
        #image = imageBig.resize(size)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        self.data[0] = normalized_image_array
        prediction = self.model.predict(self.data).tolist()
        detectedLightening = prediction[0][0] > prediction[0][1]
      #  detectedLightening = False
        return detectedLightening