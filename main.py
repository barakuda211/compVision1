import PIL
import numpy as np
from PIL import Image

def pilToNumpy(img):
    return np.array(img)

def numpyToPil(img):
    return Image.fromarray(img)

def padding(img):
    paddingSize



if __name__ == '__main__':
    img = PIL.Image.open("temp.png").convert("L")
    imgarr = pilToNumpy(img)
    print(imgarr.shape)
