import exp_news
import sys
sys.path.append("/home/norii/Desktop/VCCorp/Tool-link")
from crawler_link import crawl_link_web
sys.path.append("/home/norii/Desktop/VCCorp/Tool-link/url_news")
from json_url import in_out
from url_update import sosa_file


class export_web:

	def export_link():
		
		print("1__")
		j = []
		file = in_out.json_input()
		for f in file:

			co = crawl_link_web(f["link_domain"],f["cate_xpath"],f["links_xpath"])
			li = co.getcate()

			try:

				for l in li:
					in_out.json_output(l,f["web_name"])
					exp_news.export_ne(l,j)

			except TypeError: print("fix")
		print("end__")





