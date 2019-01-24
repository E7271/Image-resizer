from PIL import Image
import numpy as np

IMAGE_DIR = "C:/Users/Ethan's Laptop/Desktop/Python/IMAGE_DIR"
image = Image.open("C:/Users/Ethan's Laptop/Desktop/Python/IMAGE_DIR/download.png").convert('L')
resizedImage = image.resize((28,28))
resizedImage.save("C:/Users/Ethan's Laptop/Desktop/Python/IMAGE_DIR/newimagedata.png") 
array = np.array(resizedImage)
