import requests
import pandas as pd 
import time
import random
import re
import numpy as np 
import _pickle as pickle 
from tqdm import tqdm_notebook as tqdm
from bs4 import BeautifulSoup as bs 

#refreshing rate 
seq = [i/10 for i in range (8,18)]

# a list of extra curricula activities
actslist = []

# gathering activities by repeatedly refreshing the page
for _ in tqdm(range(200)):

	#actually refreshing the page
	page = requests.get("http://lab.sulko.co/designer-bio/#12-9-2-6-26-3-1-0-2-2-7")
	soup = bs(page.content, "lxml")
	#markup_type = markup_type))

	try:
		#getting one profile
		bios = soup.find('div', class_='row no-margin for -sign').findall('p')

		#adding it to the activities list
		actslist.extend([re.findall('"([^"]*)"', i.text) for i in bios])

	except:
		pass

		#sleep
		time.sleep(random.choice(seq))

#turning list into a dataframe
activity_df = pd.DataFrame(actslist, columns=['Bios'])