import numpy as np 
from math import pi,e


def G(x, y=0, variance=0.6):
	"""gaussian function"""
	return (1/ (2 * pi * variance)) * np.exp(- (x**2 + y**2)/(2 * variance))

def gaussian_kernel(kernelsize):
	"""Creates an array containing weights of a gaussian distribution"""
	gaussian_array = np.zeros(kernelsize*2 + 1)

	for i,k in zip(range(len(gaussian_array)), range(-kernelsize,kernelsize+1)):
		gaussian_array[i] = G(k)

	# normalize weights
	gaussian_array = gaussian_array / gaussian_array.sum()

	return gaussian_array


def gaussian_blur(img_array, img_size, kernelsize):
	output_array = np.copy(img_array)
	gaussian_array = gaussian_kernel(kernelsize)

	# apply gaussian blur in 2 passes, first over every row then over every column
	output_array = np.apply_along_axis(lambda arr: np.convolve(arr, gaussian_array, "same"),1,img_array)
	output_array = np.apply_along_axis(lambda arr: np.convolve(arr, gaussian_array, "same"),0,output_array)	

	return np.uint8(output_array)


def detect_edges(img_array, img_size):
	output_array = np.array(img_array, np.uint8)
	for y in range(img_size[1]):
		for x in range(img_size[0]):
			output_array[y][x] = int(img_array[y][x] * 2)
			output_array[y][x] = 255 if 150 > output_array[y][x] > 50  else 0
	return output_array