import numpy as np 

def gaussian_blur(img_array, img_size):
	output_array = [[0]*img_size[0]] * img_size[1]
	for y in range(img_size[1]):
		for x in range(img_size[0]):
			output_array[y][x] = img_array[y][x] * 2

	return output_array

def weird_hack(img_array, img_size):
	output_array = np.array(img_array, np.int8)
	for y in range(img_size[1]):
		for x in range(img_size[0]):
			output_array[y][x] = int(img_array[y][x] *2)

	return output_array