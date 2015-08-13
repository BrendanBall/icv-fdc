import numpy as np 
from math import pi,e


def G(x, y, variance=0.2):
	gaussian = [[0.1,0.1,0.1],[0.1,0.5,0.1],[0.1,0.1,0.1]]
	return (1/ (2 * pi * variance)) * e ** (- (x**2 + y**2)/(2 * variance))

def gaussian_kernel(img_array, img_size, x, y, kernelsize):
	sum = 0;
	for j in range(-kernelsize, kernelsize+1):
		for i in range(-kernelsize, kernelsize+1):
			if (y + j >= 0 and x + i >= 0 and y + j < img_size[1]  and x + i < img_size[0]):
				sum += img_array[y + j][x + i] * G(i, j)
				#print i+x,j+y, img_array[y + j][x + i] * G(i, j), G(i, j)

	#print sum
	#if sum > 0:
		#print sum
	return int(sum)





def gaussian_blur(img_array, img_size, kernelsize):
	output_array = np.copy(img_array)
	for y in range(img_size[1]):
		for x in range(img_size[0]):

			output_array[y][x] = gaussian_kernel(img_array, img_size, x, y, kernelsize)


	return output_array



def weird_hack(img_array, img_size):
	output_array = np.array(img_array, np.int8)
	for y in range(img_size[1]):
		for x in range(img_size[0]):
			output_array[y][x] = int(img_array[y][x] * 2)

	return output_array