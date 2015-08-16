from math import sqrt, pi, cos, sin
import numpy as np

def accumulate(edge_array, img_size):
	max_radius = int(sqrt(img_size[0]**2 + img_size[1]**2))
	accumulater_array = np.zeros((img_size[1], img_size[0]), dtype=np.uint32)

	for y in range(img_size[1]):
		for x in range(img_size[0]):
			if edge_array[y][x] == 255:
				for theta in range(360):
					radians = (theta * pi)/180
					x_acc = int(round(x - 30.5 * cos(radians)))
					y_acc = int(round(y - 30.5 * sin(radians)))
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


	maxima = [(0,x,y),(0,x,y),(0,x,y),(0,x,y)]

	for y in range(img_size[1]):
		for x in range(img_size[0]):
			for i in range(len(maxima) -1,-1, -1):
				if accumulater_array[y][x] > maxima[i][0]:
					if i > 0 and accumulater_array[y][x] < maxima[i-1][0]:
						maxima[i] = (accumulater_array[y][x],x,y)
						break
					

	print maxima
	return accumulater_array