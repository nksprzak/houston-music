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
			'https://www.songkick.com/venues/3357044-smart-financial-centre/calendar',
			'https://www.songkick.com/venues/9786-stereo-live/calendar',
			'https://www.songkick.com/venues/492-cynthia-woods-mitchell-pavilion/calendar',
			'https://www.songkick.com/venues/646361-fitzgeralds/calendar',
			'https://www.songkick.com/venues/11403-firehouse-saloon/calendar'
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = '%s.html' % page
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)