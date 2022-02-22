
from scrapyPageObjects.spiders.rootPage import RootPage

class BTSBookPage(RootPage):
    """Logic to extract book info from pages like https://books.toscrape.com/catalogue/soumission_998/index.html"""
    def to_item(self):

        data = dict()

        data['Site'] = 'bts'
        data['URL'] = self.url
        data['Name'] = self.css("title::text").get()

        return data
        # return {
        #     'url': self.url,
        #     'name': self.css("title::text").get(),
        # }
