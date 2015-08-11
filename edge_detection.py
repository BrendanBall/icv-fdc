
class EdgeDetection:
	def __init__(self, img_array):
		self.img_array = img_array


	def gaussian_blur(self, window_size):
		gaussian = [ 0.05,0.05,0.05,
					 0.05,0.6, 0.05, 
					 0.05,0.05,0.05]
		output_array = [None] * len(self.img_array)
		for i in range(len(self.img_array)):
			output_array[i] = self.img_array[i] * 2
		return output_array
