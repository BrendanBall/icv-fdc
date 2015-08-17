from PIL import Image, ImageOps, ImageDraw
import PIL
import sys
import numpy as np
from edge_detection import *
from hough_transform import *
import hough_transform_fast as htf
import argparse
import os


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


def save_image(image, filename, description):
	directory = "saved_images"
	if not os.path.exists(directory):
		os.makedirs(directory)

	basename = os.path.basename(filename)
	basename = os.path.splitext(basename)[0]
	newname = "%s_%s.gif" % (basename, description)
	path = os.path.join(directory, newname)
	image.save(path)



def edge_detection_optimized(filename, slow=False, radius=None, save=False):
	img = Image.open(filename).convert("L")
	img.show()
	img_array = np.array(img, np.uint8).reshape(img.size[1], img.size[0])
	print "loaded the image"

	if slow:
		blurred_array = gaussian_blur(img_array, img.size, 2)
	else:
		blurred_array = gaussian_blur_optimized(img_array, img.size, 2)
	blurred_img = Image.fromarray(blurred_array)
	blurred_img.show()
	print "performed a gaussian blur on the image"

	edge_array = detect_edges(blurred_array, img.size)
	edge_array_bool = convert_edge_boolean_array(edge_array, img.size)
	edge_img = Image.fromarray(edge_array)
	edge_img.show()
	print "performed edge detection on the image"

	if radius is not None:
		circles, accumulater_array = accumulate(edge_array, img.size, radius)
	else:
		circles, accumulater_array = htf.accumulate(edge_array_bool, img.size)

	accumulate_img = Image.fromarray(np.uint8(accumulater_array))
	accumulate_img.show("accumulated")
	print "performed hough transform"

	#draw circles
	img = img.convert("RGB")
	draw = ImageDraw.Draw(img)
	for circle in circles:
		circle_points = drawing_points(circle)
		draw.ellipse(circle_points, outline="#AB0000")
	img.show()
	print "highlighted circles on original image"


	if save:
		save_image(blurred_img, filename, "smoothed")
		save_image(edge_img, filename, "edges")
		save_image(accumulate_img, filename, "accumulated")
		save_image(img, filename, "circles_highlighted")



if __name__ == "__main__":
	description = "Simple circle detector. Detects circles in images and highlights them"
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument("--slow", action="store_true",help="If you want to use the naive gaussian blur which is very slow then go ahead")
	parser.add_argument("-r","--radius", type=int, help="Detect circles of specific radius. Uses naive hough transform")
	parser.add_argument("filename", help="filename of the image you want to process")
	parser.add_argument("--save", action="store_true", help="Save the files to disk instead of just view them temporarily")

	
	args = parser.parse_args()
	

	edge_detection_optimized(args.filename, args.slow, args.radius, args.save)