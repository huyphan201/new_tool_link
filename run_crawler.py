import json
import os
import requests
from lxml.html import fromstring
from apscheduler.schedulers.blocking import BlockingScheduler
#############################
import sys  
sys.path.append("/home/norii/Desktop/VCCorp/Tool-link/crawler")
from export_wb import export_web

def run():
	export_web.export_link()


try:
	# Trinh hen lich chay
	scheduler = BlockingScheduler()
	scheduler.add_job(run,'interval',minutes=15)
	print("tientrinh!")
	scheduler.start()
except (KeyboardInterrupt, SystemExit):
	pass