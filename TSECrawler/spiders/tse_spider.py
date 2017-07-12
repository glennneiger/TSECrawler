import os

import scrapy, urllib

class TSESpider(scrapy.Spider):
    name = "tse"
    start_urls = ['http://www.tse.jus.br/hotSites/pesquisas-eleitorais/index.html']
    allowed_domains = ['agencia.tse.jus.br', 'www.tse.jus.br']

    def parse(self, response):
        # follow pagination links
        for link in response.css('a::attr(href)'):
            href = link.extract()
            if href.find('.zip') != -1:
                self.retrieve_file(href)
            elif href.find('.html') != -1:
                yield response.follow(link, self.parse)

    def retrieve_file(self, href):
        file = 'output/' + '/'.join(href.split("/")[-2:])
        directory = os.path.dirname(file)
        if not os.path.exists(directory): os.makedirs(directory)

        if os.path.exists(file):
            print 'Skipping %s' % file
        else:
            print 'Downloading %s from %s' % (file, href)
            urllib.urlretrieve(href, file)
            print 'Saved %s from %s' % (file, href)
