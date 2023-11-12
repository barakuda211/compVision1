import PIL
import sys
import numpy as np
from PIL import Image

def pilToNumpy(img):
    return np.array(img)

def numpyToPil(img):
    output = Image.fromarray(img)
    if output.mode != 'RGB':
        output = output.convert('RGB')
    return output

def padding(img):
    paddingSize = 2
    maxImgSize = max(img.shape)
    while maxImgSize > paddingSize:
        paddingSize *= 2

    paddingImg = np.zeros([paddingSize,paddingSize,3],dtype=np.uint8)
    xShift = (paddingSize - img.shape[0]) // 2
    yShift = (paddingSize - img.shape[1]) // 2
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            paddingImg[xShift+i][yShift+j] = img[i][j]
    return paddingImg

def testPadding():
    np.set_printoptions(threshold=sys.maxsize)

    img = PIL.Image.open("500x500.png").convert("RGB")
    imgarr = pilToNumpy(img)
    print(imgarr.shape)

    paddingImg = padding(imgarr)
    pilImg = numpyToPil(paddingImg)
    pilImg.save("paddingOutput.jpg")

if __name__ == '__main__':
    testPadding()
