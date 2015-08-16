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


def circle_coords(center, radius):
	x1, y1 = center[0] - radius, center[1] - radius
	x2, y2 = center[0] + radius, center[1]+ radius
	return [x1,y1,x2,y2]

def edge_detection_optimized():
	img = Image.open(sys.argv[1]).convert("L")
	#img.show()
	img_array = np.array(img, np.uint8).reshape(img.size[1], img.size[0])

	blurred_array = gaussian_blur_optimized(img_array, img.size, 2)
	blurred_img = Image.fromarray(blurred_array)
	blurred_img.show()

	edge_array = detect_edges(blurred_array, img.size)
	edge_img = Image.fromarray(edge_array)
	edge_img.show()
"""
	accumulator_array, circle_center = accumulate(edge_array, img.size)
	accumulate_img = Image.fromarray(np.uint8(accumulator_array))
	accumulate_img.show("accumulated")
	img = img.convert("RGB")
	draw = ImageDraw.Draw(img)
	radius = 30.5
	circle = circle_coords(circle_center, radius)
	draw.ellipse(circle, outline="blue")
	img.show()"""




if __name__ == "__main__":
	edge_detection_optimized()