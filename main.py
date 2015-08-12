from PIL import Image
import PIL
import sys
import numpy as np
from edge_detection import weird_hack


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
	weird_edgedet()