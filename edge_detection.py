def gaussian_blur(img_array, img_size):
	output_array = [None] * len(img_array)
	for i in range(len(img_array)):

		output_array[i] = img_array[i] * 2
	return img_array
