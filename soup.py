from bs4 import BeautifulSoup
import os,glob,json

files = []

os.chdir("/home/nkasprzak/houston-music/songkick")
for file in glob.glob("*.html"):
    files.append(file)

for venue in files:

	soup = BeautifulSoup(open("/home/nkasprzak/houston-music/songkick/%s" % venue), "html.parser")

	for li in soup.find_all('li'):
		if li.get('title') != None:
			time = li.find('time').get('datetime')
			band = li.find('p').find('strong').get_text()
			venue_name = li.find('p').find_next('p').find('a').get_text()
			json = {'band' : band, 'time' : time, 'venue' : venue_name}
			print json
	
	print '\n'
