# 
# File Name: main.py
#
# Execution Steps:
#  bash python <main.py> <Output Directory>
# Example:
#  bash python main.py downloads/python
#
# 
# ==========================================================================================
# Modified By			Modified On (DD/MM/YY)			Version		Comments
#	ABHISHEK				08/06/17						1.0		Created
#
# SYSTEM REQUIREMENTS : 1. requests module 
#						2. lxml module 



import json
import datetime
import urls
import os
import sys
from scrappy import scrape_all_diesel_prices
from scrappy import scrape_all_petrol_prices

def file_generation():
	if (len(sys.argv) != 2):
		ts = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
		print (ts,"\t[ERROR] Invalid Number Of Arguments")
		print ("========================== END",datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")," ==========================")
		exit()
	file_path = sys.argv[1]
	if not os.path.exists(file_path):

		ts = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
		print (ts,"\t[ERROR] Directory Doesnt Exist")
		print (ts,"\t[ERROR] Quitting\n\n")

	else:		
		with open(os.path.join(file_path, 'diesel_price.json'), 'w') as f:
  			json.dump(scrape_all_diesel_prices(), f, ensure_ascii=False)

		ts = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")	
		print (ts,"\t[SUCCESS] Diesel Prices Generated")   

		with open(os.path.join(file_path, 'petrol_price.json'), 'w') as f:
  			json.dump(scrape_all_petrol_prices(), f, ensure_ascii=False) 

		ts = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
		print (ts,"\t[SUCCESS] Petrol Prices Generated\n\n")   



if __name__ == "__main__":

	
	print ("========================== BEGIN",datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"),"==========================")
	file_generation();
	print ("========================== END",datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"),"==========================")