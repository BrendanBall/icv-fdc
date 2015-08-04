from PIL import Image
import PIL
import sys
import numpy as np



if __name__ == "__main__":
	im = Image.open(sys.argv[1]).convert("L")
	nparr = np.asarray(im, dtype=np.uint8).T
	im = PIL.Image.fromarray(np.uint8(nparr.T))
