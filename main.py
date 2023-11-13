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

def padding(img, paddingSize):
    paddingImg = np.zeros([paddingSize,paddingSize,3], dtype=np.uint8)
    xShift = (paddingSize - img.shape[0]) // 2
    yShift = (paddingSize - img.shape[1]) // 2
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            paddingImg[xShift+i][yShift+j] = img[i][j]
    return paddingImg

def pooling(img):
    xSize = img.shape[0] // 2 + img.shape[0] % 2
    ySize = img.shape[1] // 2 + img.shape[1] % 2
    outputMax = np.zeros([xSize, ySize, 3], dtype=np.uint8)
    outputMin = np.zeros([xSize, ySize, 3], dtype=np.uint8)
    outputAvg = np.zeros([xSize, ySize, 3], dtype=np.uint8)

    for i in range(0,img.shape[0], 2):
        for j in range(0, img.shape[1], 2):
            for k in range(3):
                temp = img[i:i+2:1,j:j+2:1,k].ravel()
                outputMax[i // 2, j // 2, k] = max(temp)
                outputMin[i // 2, j // 2, k] = min(temp)
                outputAvg[i // 2, j // 2, k] = sum(temp)//4

    return [outputMax, outputMin, outputAvg]

def kernelСonvolution(img, kernel):
    kernelSize = kernel.shape[0]
    xSize = img.shape[0] - kernelSize + 1
    ySize = img.shape[1] - kernelSize + 1
    outputKernel = np.zeros([xSize, ySize], dtype=np.uint8)

    for i in range(0, xSize):
        for j in range(0, ySize):
            temp = img[i:i + kernelSize:1, j:j + kernelSize:1]
            outputKernel[i, j] = np.uint8(min(255, np.dot(temp, kernel).ravel().sum()))
    return outputKernel



def testPadding(imgName, size):
    img = PIL.Image.open(imgName).convert("RGB")
    imgarr = pilToNumpy(img)

    paddingImg = padding(imgarr, size)
    pilImg = numpyToPil(paddingImg)
    pilImg.save("paddingOutput.png")

def testPooling(imgName):
    img = PIL.Image.open(imgName).convert("RGB")
    imgarr = pilToNumpy(img)

    poolingImages = pooling(imgarr)
    numpyToPil(poolingImages[0]).save("maxPolling.png")
    numpyToPil(poolingImages[1]).save("minPolling.png")
    numpyToPil(poolingImages[2]).save("avgPolling.png")

def testKernelСonvolution(imgName):
    img = PIL.Image.open(imgName).convert("L")
    imgarr = pilToNumpy(img)

    kernelImage = kernelСonvolution(imgarr, np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]))
    numpyToPil(kernelImage).save("kernelConvlution.png")


if __name__ == '__main__':
    testPadding("500x500.png", 600)
    testPooling("500x500.png")
    testKernelСonvolution("logo.jpg")
