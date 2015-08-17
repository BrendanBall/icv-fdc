import math
import numpy as np
import itertools
from collections import deque
from operator import itemgetter

def accumulate(edge_array, img_size, threshold):
	accumulater_array = np.zeros((img_size[1], img_size[0]), dtype=np.uint32)

	global_point_set = set()
	maxima = []

	for y in range(img_size[1]):
		for x in range(img_size[0]):
			if edge_array[y][x] and (x,y) not in global_point_set:
				# create a graph of all the points connected to the current point
				local_point_set = connect_points(edge_array, img_size, (x,y))
				global_point_set = global_point_set.union(local_point_set)
				if len(local_point_set) > 10:
					xmin = min(local_point_set, key=itemgetter(0))[0]
					ymin = min(local_point_set, key=itemgetter(1))[1]
					xmax = max(local_point_set, key=itemgetter(0))[0]
					ymax = max(local_point_set, key=itemgetter(1))[1]

					radius = (ymax - ymin) // 2

					# make bounding box slightly bigger on all sides for better fit
					for i in range(1,3):
						if point_in_array(edge_array, img_size, (xmin-i,0)):
							xmin = xmin-i
						if point_in_array(edge_array, img_size, (0,ymin-i)):
							ymin = ymin-i
						if point_in_array(edge_array, img_size, (xmax+i,0)):
							xmax = xmax+i
						if point_in_array(edge_array, img_size, (0,ymax+i)):
							ymax = ymax+i
						
					bounding_box_top = (xmin, ymin)
					bounding_box_bot = (xmax, ymax)

					accumulate_region(edge_array, accumulater_array, img_size, radius, bounding_box_top, bounding_box_bot)
					local_maxima = find_local_maxima(accumulater_array, img_size, radius, threshold,bounding_box_top, bounding_box_bot)
					maxima.extend(local_maxima)





	#normalize
	max_accumulate = accumulater_array.max()
	print "max: ",max_accumulate
	if max_accumulate > 255:
		ratio = max_accumulate / float(255)
		accumulater_array = accumulater_array / ratio


	return (maxima, accumulater_array, max_accumulate)


def connect_points(edge_array, img_size, p0):
	"""Performs a depth first search to find all connected points to a given point.
		This should connect all points for a circle"""
	local_point_set = set()
	stack = deque()
	stack.append(p0)

	while stack:
		point = stack.pop()
		if point not in local_point_set:
			local_point_set.add(point)
			for y in range(point[1]-1, point[1] + 2):
				for x in range(point[0]-1, point[0] + 2):
					if validate_point(edge_array, img_size, (x,y), local_point_set):
						stack.append((x,y))
	return local_point_set

def point_in_array(edge_array, img_size, p):
	if p[0] >= 0 and p[0] < img_size[0] and p[1] >= 0 and p[1] < img_size[1]:
		return True

def validate_point(edge_array, img_size, p, visited):
	if p[0] >= 0 and p[0] < img_size[0] and p[1] >= 0 and p[1] < img_size[1] and p not in visited:
		return edge_array[p[1]][p[0]]
	else:
		return False


def accumulate_region(edge_array, accumulater_array, img_size, radius, region_top, region_bot):

	for y in xrange(region_top[1], region_bot[1]):
		for x in range(region_top[0], region_bot[0]):
			if edge_array[y][x]:
				for theta_d in range(360):
					theta_r = np.radians(theta_d)
					x_acc = int(round(x + radius * np.cos(theta_r)))
					y_acc = int(round(y + radius * np.sin(theta_r)))
					if x_acc < img_size[0] and x_acc >= 0 and y_acc < img_size[1] and y_acc >= 0:
						accumulater_array[y_acc][x_acc] += 1


def find_local_maxima(arr, img_size, radius, threshold, region_top, region_bot):
	"""Finds the points in the region above the specified threshold. These points should be circles"""
	maxima = []
	for y in range(region_top[1], region_bot[1]):
		for x in range(region_top[0], region_bot[0]):
			if arr[y][x] > threshold:
				maxima.append((x, y, radius,arr[y][x]))
	return maxima
