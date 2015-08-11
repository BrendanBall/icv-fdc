from PIL import Image
import PIL
import sys
import numpy as np
from edge_detection import EdgeDetection


if __name__ == "__main__":
	im = Image.open(sys.argv[1]).convert("L")
	img_array = list(im.getdata())
	im.show()
	edge_det = EdgeDetection(img_array)
	blurred_array = edge_det.gaussian_blur(3) 
	blurred_img = Image.new("L", im.size)
	blurred_img.putdata(blurred_array)
	blurred_img.show()

