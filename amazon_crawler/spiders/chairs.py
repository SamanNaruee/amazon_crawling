import scrapy


class ChairsSpider(scrapy.Spider):
    name = "chairs"
    allowed_domains = ["www.amazon.de"]
    start_urls = ["https://www.amazon.de/s?k=chair&crid=33QV1W0ICPY5V&sprefix=chai%2Caps%2C211&ref=nb_sb_ss_ts-doa-p_3_4"]

    def parse(self, response):
        pass
