import os

class sosa_file:
	'''SO SÁNH URL MỚI VÀ CŨ'''

	def url_up():

		path = "/home/norii/Desktop/VCCorp/Tool-link/data/output/data_link/{}".format("tienphong")

		for i in os.listdir(path):
			
			with open(path+'/'+i,'r') as f:
				t =f.read()

			return t


	def url_if(new,old):

		if new != old: return new

		else: print("Url trùng!")

