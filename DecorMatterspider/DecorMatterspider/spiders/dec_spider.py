from scrapy.spiders import Spider

from scrapy.selector import Selector

from DecorMatterspider.items import DecormatterspiderItem

class decspider(Spider):
    name="dec_pic_spider"
    allowed_domains = ["decormatters.com"]
    start_urls=[
        'http://decormatters.com/'
    ]
    
    def parse(self,response):
        for sel in response.xpath('//img'):
            link = str(sel.xpath('@src').extract()[0])
            image = DecormatterspiderItem()
            url = 'http://decormatters.com/' + link
            print 'the urls:/n'
            print url
            print '\n'
            image['image_urls'] = [url]
            yield image