"""
Scrapy spider which uses Page Objects both for crawling and extraction,
and uses overrides to support two different sites without changing
the crawling logic (the spider is exactly the same)

No configured default logic: if used for an unregistered domain, no logic
at all is applied.
"""
import scrapy

from scrapyPageObjects.spiders.pages.bts.bts_page import BTSBookPage
from scrapyPageObjects.spiders.pages.cricinfo.cricInfo_page import CricInfoPage
from scrapyPageObjects.spiders.pages.berry_lush.berry_lush_page import BerryLushPage
from scrapyPageObjects.spiders.rootPage import RootPage
import pandas as pd

from scrapyPageObjects.utils.writer import WriteData

class GenericSpider(scrapy.Spider):
    name = 'generic_spider'

    def getLinks(self, site):
        links = []
        df = pd.read_csv('C:\\scrapyPageObjects\\scrapyPageObjects\\spiders\\pages\\' + site + '\\links.csv')
        n = len(df['Url'])
        print(n)

        for i in range(n):   
            try:
                links.append(df['Url'][i])
            except Exception as e:
                    print(e)
        return links

    def __init__(self, category=None, *args, **kwargs):
        super(GenericSpider, self).__init__(*args, **kwargs)

        try:
            self.start_urls = self.getLinks(self.site)
        except Exception as e:
            print(e)

    def parse(self, response, page: RootPage):
        data = page.to_item()
        yield data
        wd = WriteData
        wd.writedata(self, data)