import numpy as np
from PIL import Image
from pylab import *
import copy
import math
from scipy.signal import convolve2d

def horizonralFilter(imageArray): 

	horizonralFilterArray = np.array([[-1,0,1],[-2,0,2], [-1,0,1]]) / 4

	newImageArray = copy.deepcopy(imageArray)
	border = horizonralFilterArray.shape[0] // 2

	for i in range(border, imageArray.shape[0] - border):
		for j in range(border, imageArray.shape[1] - border):
			sum = 0 
			for x in range(horizonralFilterArray.shape[0]):
				for y in range(horizonralFilterArray.shape[1]):
					sum += horizonralFilterArray[x][y] * imageArray[i - x + 1][j - y + 1]
			newImageArray[i][j] = math.sqrt(sum ** 2)
	
	return newImageArray

def verticalFilter(imageArray): 
	verticalFilterArray = np.array([[-1,-2,-1],[0,0,0], [1,2,1]]) / 4

	newImageArray = copy.deepcopy(imageArray)

	border = verticalFilterArray.shape[0] // 2
	for i in range(border, imageArray.shape[0] - border):
		for j in range(border, imageArray.shape[1] - border):
			sum = 0 
			for x in range(verticalFilterArray.shape[0]):
				for y in range(verticalFilterArray.shape[1]):
					sum += verticalFilterArray[x][y] * imageArray[i - x + 1][j - y + 1]
			newImageArray[i][j] = math.sqrt(sum ** 2)
	
	return newImageArray

image = Image.open('test.jpg').convert('L')
imageArray = np.array(image)

hImage = horizonralFilter(imageArray)
vImage = verticalFilter(imageArray)

newvImage = Image.fromarray(vImage)
newhImage = Image.fromarray(hImage)


newImg = np.add(newhImage, newvImage)

Image.fromarray(newImg).convert('L').save('newOne.jpg')



