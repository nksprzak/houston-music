# houston-music
This is an aggregator of all the music going on in Houston weekly.

## Things needed to be done:
	1. Make a web scrapper
	2. Determine all the venues needed to be scrapped
	3. Put all the data into the following JSON format
		* Band
		* Date
		* Time
		* Venue
		* Link to tickets (if available)
	4. Parse data into a usable Google Doc excel sheet or website.


## Advanced aspects
	1. Upcoming acts whose tickets are going on sale that week
	2. Spotify links to the artists as another part of the JSON.


## How to run the code so far:
	1. clone the repo
	2. install scrapy && install beautiful soup
	3. cd into songkick dir
	4. run the command 'scrapy crawl songkick'
	5. cd to project root
	6. run soup.py
	7. creates a JSON songkick_data.txt in the songkick dir

## How to delete the HTML that are scrapped:
	find . -type f -iname "*.html" -delete