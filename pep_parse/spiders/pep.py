import scrapy
from scrapy.exceptions import DropItem
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        section = response.css('section#index-by-category')

        tbody = section.css('tbody')
        tr_all = tbody.css('tr')

        for tr in tr_all:
            pep_link = tr.css('a[href^="pep"]::attr(href)').extract_first()
            columns = tr.css('a::text').getall()
            if columns:
                number = columns[0].strip()
                name = (columns[1].strip(),)
            else:
                raise DropItem('Ошибка данных')

            yield response.follow(
                pep_link,
                callback=self.parse_pep,
                meta={'number': number, 'name': name},
            )

    def parse_pep(self, response):
        status = response.css('abbr::text').get().strip()
        data = {
            'number': response.meta['number'],
            'name': response.meta['name'],
            'status': status,
        }
        yield PepParseItem(data)
