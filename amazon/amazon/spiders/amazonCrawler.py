import scrapy


class AmazoncrawlerSpider(scrapy.Spider):
    name = "amazonCrawler"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456&ref=nav_em__nav_desktop_sa_intl_computer_accessories_and_peripherals_0_2_6_2"]

    def parse(self, response):
        pass
