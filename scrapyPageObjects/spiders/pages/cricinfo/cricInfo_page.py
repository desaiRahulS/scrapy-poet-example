from scrapyPageObjects.spiders.rootPage import RootPage

class CricInfoPage(RootPage):
    def to_item(self):
        # return {
        #     'url': self.url,
        #     'name': self.xpath("//a[@title='Live Scores']/text()").get(),
        # }
        data = dict()

        data['Site'] = 'cricinfo'
        data['URL'] = self.url
        data['Name'] =  self.xpath("//a[@title='Live Scores']/text()").get()

        return data