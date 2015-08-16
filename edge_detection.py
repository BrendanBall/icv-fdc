import numpy as np 
from math import pi,e


def G(x, y=0, variance=0.6):
	"""gaussian function"""
	return (1/ (2 * pi * variance)) * np.exp(- (x**2 + y**2)/(2 * variance))

def gaussian_kernel(kernelsize):
	"""Creates a 1d array containing weights of a gaussian distribution"""
	gaussian_array = np.zeros(kernelsize*2 + 1)

	for i,k in zip(range(len(gaussian_array)), range(-kernelsize,kernelsize+1)):
		gaussian_array[i] = G(k)

	# normalize weights
	gaussian_array = gaussian_array / gaussian_array.sum()

	return gaussian_array


def gaussian_blur(img_array, img_size, kernelsize):
	"""Uses a 1d gaussian array to apply smoothing. This method implements it naively and is quite slow in python"""
	xpass_array = np.zeros((img_size[1], img_size[0]), dtype=np.uint8)
	ypass_array = np.zeros((img_size[1], img_size[0]), dtype=np.uint8)
	gaussian_array = gaussian_kernel(kernelsize)
	windowsize = kernelsize * 2 + 1

	# apply gaussian blur in 2 passes, first over every row then over every column
	# passing over rows
	for j in xrange(img_size[1]):
		for i in range(img_size[0]):
			sum = 0
			for k,w in zip(range(-kernelsize, kernelsize+1), range(windowsize)):
				x = i + k
				if x >= 0 and x < img_size[0]:
					sum += img_array[j][x] * gaussian_array[w] 
			xpass_array[j][i] = int(sum)

	# passing over columns
	for i in xrange(img_size[0]):
		for j in range(img_size[1]):
			sum = 0
			for k,w in zip(range(-kernelsize, kernelsize+1), range(windowsize)):
				y = j + k
				if y >= 0 and y < img_size[1]:
					sum += xpass_array[y][i] * gaussian_array[w] 
			ypass_array[j][i] = int(sum)

	output_array = ypass_array

	return np.uint8(output_array)
	


def gaussian_blur_optimized(img_array, img_size, kernelsize):
	"""Performs same operation as gaussian_blur but makes use of numpy vectorization to optimize for speed"""
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





def median_kernel(img_array, img_size, x, y, kernelsize):
	window = []
	i = 0
	for j in range(-kernelsize, kernelsize+1):
		for i in range(-kernelsize, kernelsize+1):
			if (y + j >= 0 and x + i >= 0 and y + j < img_size[1]  and x + i < img_size[0]):
				window.append(img_array[y + j][x + i])
				i += 1

	window.sort()
	return window[i/2 +1]


def median_filter(img_array, img_size, kernelsize):
	output_array = np.copy(img_array)
	for y in range(img_size[1]):
		for x in range(img_size[0]):

			output_array[y][x] = median_kernel(img_array, img_size, x, y, kernelsize)


	return output_array