from bs4 import BeautifulSoup
import os,glob,json

files = []
data = []

os.chdir("%s/houston-music/songkick" % os.path.expanduser('~'))
for file in glob.glob("*.html"):
    files.append(file)

for venue in files:

	soup = BeautifulSoup(open("%s/houston-music/songkick/%s" % (os.path.expanduser('~'), venue)), "html.parser")

	for li in soup.find_all('li'):
		if li.get('title') != None:
			time = li.find('time').get('datetime')
			band = li.find('p').find('strong').get_text()
			venue_name = li.find('p').find_next('p').find('a').get_text()
			link = "https://www.songkick.com%s" % li.find('a').get('href')
			entry = {'band' : band, 'time' : time, 'venue' : venue_name, 'link' : link}
			data.append(entry)
	
with open('songkick_data.txt', 'w') as outfile:
    json.dump(data, outfile)
