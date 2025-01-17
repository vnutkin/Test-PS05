import scrapy


class MydivannewparsSpider(scrapy.Spider):
    name = "mydivannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru/sankt-peterburg/category/svet"]

    def parse(self, response):
        lamps = response.css('div.WdR1o')
        print(f'найдено {len(lamps)}')
        for lamp in lamps:
            yield {
            # Ссылки и теги получаем с помощью консоли на сайте
            # Создаём словарик названий, используем поиск по диву, а внутри дива — по тегу span
                'name': lamp.css('div.lsooF span::text').get(),
            # Создаём словарик цен, используем поиск по диву, а внутри дива — по тегу span
                'price': lamp.css('div.pY3d2 span::text').get(),
             #   'price': lamp.css('div.q5Uds span::text').get(),
            # Создаём словарик ссылок, используем поиск по тегу "a", а внутри тега — по атрибуту
            # Атрибуты — это настройки тегов
                'url': lamp.css('a').attrib['href']
            }
   
