import math
import numpy as np

def accumulate(edge_array, img_size, threshold=200):
	max_radius = int(math.sqrt(img_size[0]**2 + img_size[1]**2))
	accumulater_array = np.zeros((img_size[1], img_size[0]), dtype=np.uint32)
	radius = 20
	for y in range(img_size[1]):
		for x in range(img_size[0]):
			if edge_array[y][x] == 255:
				for theta_d in range(360):
					radians = np.radians(theta_d)
					x_acc = int(round(x - radius * np.cos(radians)))
					y_acc = int(round(y - radius * np.sin(radians)))
					if x_acc < img_size[0] and x_acc >= 0 and y_acc < img_size[1] and y_acc >= 0:
						accumulater_array[y_acc][x_acc] += 1

	max = 0
	for y in range(img_size[1]):
		for x in range(img_size[0]):
			if accumulater_array[y][x] > max:
				max =  accumulater_array[y][x]

	for y in range(img_size[1]):
		for x in range(img_size[0]):
			v = int((accumulater_array[y][x]/float(max)) * 255)


	
	maxima = find_maxima(accumulater_array, img_size, threshold)
	print maxima
	return (accumulater_array, maxima)


def find_maxima(arr, img_size, threshold):
	"""Finds the points in the array above the specified threshold. These points should be circles"""
	maxima = []
	for y in range(img_size[1]):
		for x in range(img_size[0]):
			if arr[y][x] > threshold:
				maxima.append((x, y, 32,arr[y][x]))
	return maxima