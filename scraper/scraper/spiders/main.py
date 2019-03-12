import scrapy
from scraper.items import HouseItem


filename = "rental_list.txt"

class TerenceSpider(scrapy.Spider):
    name = "my_spider"

    def start_requests(self):
        urls = [
            'https://vancouver.craigslist.org/search/apa?s=0',
            'https://vancouver.craigslist.org/search/apa?s=120',
            # 'https://vancouver.craigslist.org/search/apa?s=240',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        search_results = response.css(".result-row")        

        for item in search_results:
            title = item.css('.result-title::text').extract_first()
            price = item.css('.result-price::text').extract_first()
            link = item.css('.result-title::attr(href)').extract_first()


            house_item = HouseItem()

            house_item['title'] = title
            house_item['price'] = price
            house_item['link'] = link

            yield house_item

        # with open(filename, 'a+') as f: