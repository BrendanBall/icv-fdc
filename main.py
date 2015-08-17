from PIL import Image, ImageOps, ImageDraw
import PIL
import sys
import numpy as np
from edge_detection import *
from hough_transform import *
import hough_transform_fast as htf




def edge_detection():
	img = Image.open(sys.argv[1]).convert("L")
	#img.show()
	img_array = np.array(img, np.uint8).reshape(img.size[1], img.size[0])
	#blurred_array = gaussian_blur(img_array, img.size, 1)
	##blurred_array = median_filter(blurred_array, img.size, 1)
	#edge_array = detect_edges(blurred_array, img.size)
	edge_array = img_array
	edge_img = Image.fromarray(np.uint8(edge_array))
	edge_img.show("edges")
	accumulator_array = accumulate(edge_array, img.size)
	accumulate_img = Image.fromarray(np.uint8(accumulator_array))
	accumulate_img.show("accumulated")


def drawing_points(circle):
	"""circle is a tuple of form (center x,center y, radius)"""
	x1, y1 = circle[0] - circle[2], circle[1] - circle[2]
	x2, y2 = circle[0] + circle[2], circle[1] + circle[2]
	return [x1,y1,x2,y2]


def convert_edge_boolean_array(arr, img_size):
	bool_array = np.zeros((img_size[1], img_size[0]), dtype=bool)

	for y in range(img_size[1]):
		for x in range(img_size[0]):
			if arr[y][x] == 255:
				bool_array[y][x] = True

	return bool_array


def edge_detection_optimized():
	img = Image.open(sys.argv[1]).convert("L")
	#img.show()
	img_array = np.array(img, np.uint8).reshape(img.size[1], img.size[0])

	blurred_array = gaussian_blur_optimized(img_array, img.size, 2)
	blurred_img = Image.fromarray(blurred_array)
	#blurred_img.show()

	edge_array = detect_edges(blurred_array, img.size)
	edge_array_bool = convert_edge_boolean_array(edge_array, img.size)
	edge_img = Image.fromarray(edge_array)
	edge_img.show()
	
	circles, accumulater_array, max_accumulate = htf.accumulate(edge_array_bool, img.size, 300)
	accumulate_img = Image.fromarray(np.uint8(accumulater_array))
	accumulate_img.show("accumulated")
	#circles, accumulator_arrays = hough_transform(edge_array, img.size)
	#for acc_array in accumulator_arrays:
#		accumulate_img = Image.fromarray(np.uint8(acc_array))
#		accumulate_img.show("accumulated")

	#draw circles
	img = img.convert("RGB")
	draw = ImageDraw.Draw(img)
	for circle in circles:
		circle_points = drawing_points(circle)
		draw.ellipse(circle_points, outline="#AB0000")
	img.show()




if __name__ == "__main__":
	edge_detection_optimized()