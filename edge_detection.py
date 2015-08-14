import numpy as np 
from math import pi,e


def G(x, y, variance=0.6):
	return (1/ (2 * pi * variance)) * e ** (- (x**2 + y**2)/(2 * variance))

def gaussian_kernel(img_array, img_size, x_current, y_current, kernelsize):
	sum = 0;
	for j in range(-kernelsize, kernelsize+1):
		for i in range(-kernelsize, kernelsize+1):
			x = x_current + i
			y = y_current + j
			if y < 0: 
				y = 0
			elif y >= img_size[1]:
				y = img_size[1] - 1
			if x < 0:
				x = 0
			elif x >= img_size[0]:
				x = img_size[0] - 1

			sum += img_array[y][x] * G(i, j)

	return int(sum)


def gaussian_blur(img_array, img_size, kernelsize):
	output_array = np.copy(img_array)
	for y in range(img_size[1]):
		for x in range(img_size[0]):

			output_array[y][x] = gaussian_kernel(img_array, img_size, x, y, kernelsize)


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

def detect_edges(img_array, img_size):
	output_array = np.array(img_array, np.uint8)
	for y in range(img_size[1]):
		for x in range(img_size[0]):
			output_array[y][x] = int(img_array[y][x] * 2)
			output_array[y][x] = 255 if 150 > output_array[y][x] > 50  else 0
	return output_array