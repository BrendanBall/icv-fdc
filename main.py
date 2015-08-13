from PIL import Image
import PIL
import sys
import numpy as np
from edge_detection import *


def weird_edgedet():
	im = Image.open(sys.argv[1]).convert("L")
	im.show()
	img_array = list(im.getdata())
	print im.size
	width = im.size[0]
	img_array = [img_array[i:i+width] for i in range(0, len(img_array), width)]
	blurred_array = weird_hack(img_array, im.size) 
	blurred_array = [item for sublist in blurred_array for item in sublist]
	blurred_img = Image.new("L", im.size)
	blurred_img.putdata(blurred_array)
	blurred_img.show()

if __name__ == "__main__":
	img = Image.open(sys.argv[1]).convert("L")
	img.show()
	img_array = np.array(img, np.uint8).reshape(img.size[1], img.size[0])
	#temp = np.array([[0,100,50],[20,150,75],[50,0,100]], np.uint8)
	blurred_array = gaussian_blur(img_array, img.size, 1)
	#print temp
	#print blurred_array
	blurred_array = weird_hack(blurred_array, img.size)
	blurred_img = Image.fromarray(np.uint8(blurred_array))
	blurred_img.show()