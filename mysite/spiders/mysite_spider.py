from scrapy.spiders import Spider
from scrapy.selector import Selector

from mysite.items import SimItem

class MysiteSpider(Spider):
    name = 'mysite'
    allowed_domains = ['rancho.wang']
    start_urls = [
        "http://rancho.wang/2017/06/02/simulation_7/"
    ]

    def parse(self, response):
        sel = Selector(response)
        items = []
        sites = sel.xpath('//main/article/div/p')
        print('The following are sites\n')
        print(sites)
        for site in sites:
            item = SimItem()
            item['text'] = site.xpath('text()').extract()
            items.append(item)
            print('\n******************\n')
            print(item)
        #print('The following are bodys')
        #print(response.body)
        print('The following are items \n')
        print(items)
        return items

