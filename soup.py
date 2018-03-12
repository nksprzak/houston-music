from bs4 import BeautifulSoup
import os,glob

files = []

os.chdir("/home/nkasprzak/houston-music/songkick")
for file in glob.glob("*.html"):
    files.append(file)

for venue in files:

	soup = BeautifulSoup(open("/home/nkasprzak/houston-music/songkick/%s" % venue), "html.parser")

	for li in soup.find_all('li'):
		if li.get('title') != None:
			print li.find('time').get('datetime')
			print li.find('p').find('strong').get_text()
	
	print '\n'
