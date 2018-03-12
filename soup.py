from bs4 import BeautifulSoup

soup = BeautifulSoup(open("/home/nkasprzak/houston-music/songkick/songkick-108-warehouse-live.html"), "html.parser")

for li in soup.find_all('li'):
	if li.get('title') != None:
		print li.find('time').get('datetime')
		print li.find('p').find('strong').get_text()
		print '\n'