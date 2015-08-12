from PIL import Image
import PIL
import sys
import numpy as np
from edge_detection import gaussian_blur


if __name__ == "__main__":
	im = Image.open(sys.argv[1]).convert("L")
	im.show()
	img_array = list(im.getdata())
	print im.size
	width = im.size[0]
	img_array = [img_array[i:i+width] for i in range(0, len(img_array), width)]
	print (len(img_array[0]), len(img_array))
	blurred_array = gaussian_blur(img_array, im.size) 
	blurred_img = Image.new("L", im.size)
	blurred_img.putdata([x+y for x,y in blurred_array])
	blurred_img.show()

