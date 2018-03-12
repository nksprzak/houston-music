import scrapy

class SongkickSpider(scrapy.Spider):
	name = "songkick"

	def start_requests(self):
		urls = [
			'https://www.songkick.com/venues/504-toyota-center/calendar',
			'https://www.songkick.com/venues/30866-house-of-blues/calendar',
			'https://www.songkick.com/venues/2861788-revention-music-center/calendar',
			'https://www.songkick.com/venues/108-warehouse-live/calendar',
			'https://www.songkick.com/venues/3205243-white-oak-music-hall/calendar'
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = 'songkick-%s.html' % page
		with open(filename, wb) as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)