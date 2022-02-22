from scrapyPageObjects.spiders.rootPage import RootPage

class BerryLushPage(RootPage):
    def to_item(self):
        # return {
        #     'url': self.url,
        #     'name': self.xpath("//h1/span/text()").get(),
        # }

        data = dict()

        data['Site'] = 'berry_lush'
        data['URL'] = self.url
        data['Name'] = self.xpath("//h1/span/text()").get()

        return data
