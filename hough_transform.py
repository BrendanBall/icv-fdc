import math
import numpy as np

def accumulate(edge_array, img_size, radius, threshold):
	accumulater_array = np.zeros((img_size[1], img_size[0]), dtype=np.uint32)
	for y in range(img_size[1]):
		for x in range(img_size[0]):
			if edge_array[y][x] == 255:
				for theta_d in range(360):
					theta_r = np.radians(theta_d)
					x_acc = int(round(x + radius * np.cos(theta_r)))
					y_acc = int(round(y + radius * np.sin(theta_r)))
					if x_acc < img_size[0] and x_acc >= 0 and y_acc < img_size[1] and y_acc >= 0:
						accumulater_array[y_acc][x_acc] += 1


	max_accumulate = accumulater_array.max()
	print "max: ",max_accumulate

	# find circles
	maxima = []
	if max_accumulate > threshold:
		maxima = find_maxima(accumulater_array, img_size, radius, threshold)

	#normalize
	if max_accumulate > 255:
		ratio = max_accumulate / float(255)
		accumulater_array = accumulater_array / ratio
	return (maxima, accumulater_array, max_accumulate)


def find_maxima(arr, img_size, radius, threshold):
	"""Finds the points in the array above the specified threshold. These points should be circles"""
	maxima = []
	for y in range(img_size[1]):
		for x in range(img_size[0]):
			if arr[y][x] > threshold:
				maxima.append((x, y, radius,arr[y][x]))
	return maxima


def hough_transform(edge_array, img_size, threshold=300):
	maxima = []
	accumulate_arrays = []


	i = 15
	while i < 70:
		print "radius: ", i
		maxima_list, accumulater_array, max_accumulate = accumulate(edge_array, img_size, i, threshold)
		if max_accumulate > threshold:
			maxima.extend(maxima_list)
			accumulate_arrays.append(accumulater_array)

		i += 1 if max_accumulate > 140 else 3


	return (maxima, accumulate_arrays)