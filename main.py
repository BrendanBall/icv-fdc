from PIL import Image, ImageOps, ImageDraw
import PIL
import sys
import numpy as np
from edge_detection import *
from hough_transform import *




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

def edge_detection_optimized():
	img = Image.open(sys.argv[1]).convert("L")
	#img.show()
	img_array = np.array(img, np.uint8).reshape(img.size[1], img.size[0])

	blurred_array = gaussian_blur_optimized(img_array, img.size, 2)
	blurred_img = Image.fromarray(blurred_array)
	#blurred_img.show()

	edge_array = detect_edges(blurred_array, img.size)
	edge_img = Image.fromarray(edge_array)
	#edge_img.show()

	circles, accumulator_arrays = hough_transform(edge_array, img.size)
	for acc_array in accumulator_arrays:
		accumulate_img = Image.fromarray(np.uint8(acc_array))
		accumulate_img.show("accumulated")

	#draw circles
	img = img.convert("RGB")
	draw = ImageDraw.Draw(img)
	for circle in circles:
		circle_points = drawing_points(circle)
		draw.ellipse(circle_points, outline="blue")
	img.show()




if __name__ == "__main__":
	edge_detection_optimized()