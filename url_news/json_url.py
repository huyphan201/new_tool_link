import json 
import os
from datetime import datetime
import sys
sys.path.append("/home/norii/Desktop/VCCorp/Tool-link/url_news")
from url_update import sosa_file


class in_out:

	def json_input():
		print("3__")
		
		with open("/home/norii/Desktop/VCCorp/Tool-link/data/input/input.json") as js:
			dt = json.load(js)
			doms = dt["json_web"]
			return doms


	def json_output(url, domain):

		d = "/home/norii/Desktop/VCCorp/Tool-link/data/output/data_link/{}".format(domain)
		time = datetime.now().strftime("%d%m%Y")

		for ur in url:

			old = sosa_file.url_up()
			ss_ur = sosa_file.url_if(ur,old)
			
			os.makedirs(d, mode=0o777, exist_ok=True)
			with open(d+"/_{}_data.txt".format(time),'a') as f:
				f.write(ss_ur+"\n")
