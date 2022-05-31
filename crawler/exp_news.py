from datetime import datetime
import json
import os
import sys
sys.path.append("/home/norii/Desktop/VCCorp/Tool-link")
from crawler_web import crawler_news
sys.path.append("/home/norii/Desktop/VCCorp/Tool-link/url_news")
from json_url import in_out
from url_update import sosa_file


def export_ne(l,j):
	
	print("4__")

	for ur in l:
		file = in_out.json_input()
		old = sosa_file.url_up()
		ss_ur = sosa_file.url_if(ur,old)
		
		for f in file:
			news = crawler_news(f["link_domain"],
				f["title_select"],
				f["description_select"],
				f["content_select"],
				f["image_xpath"],
				f["time_select"],
				f["author_select"],
				f["tags_select"])

			t = "/home/norii/Desktop/VCCorp/Tool-link/data/output/data_news/%s" %(f["web_name"])
			ne = news.crawler_news(ss_ur)
			j.append(ne)
			
			os.makedirs(t, mode=0o777, exist_ok=True)
			with open(t+"/%s_data.json" %(datetime.now().strftime("%d%m%Y")), "a", encoding="utf-8") as nf:
				json.dump(j, nf, indent=4,ensure_ascii=False)


