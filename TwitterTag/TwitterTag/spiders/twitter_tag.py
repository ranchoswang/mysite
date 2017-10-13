from scrapy.spiders import Spider
from scrapy.selector import Selector

from TwitterTag.items import TwitterItem




class MysiteSpider(Spider):
    name = "twitterTags"
    allowed_domains = ["trends24.in"]
    start_urls = [
        "http://trends24.in/united-states"
    ]

    def parse(self, response):
        sel = Selector(response)
        items = []
        sites = sel.xpath("//div[@class='trend-card']")
        for site in sites:
            item = TwitterItem()
            item["timeStamp"] = site.xpath("h5/@data-timestamp").extract()
            item["tag"] = site.xpath("ol/li/a/text()").extract()
            items.append(item)
        return items
