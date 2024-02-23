import scrapy
from ..items import MyScrapyProjectItem

class AmazonHeadphoneSpider(scrapy.Spider):
    name = 'amazon_headphone_spider'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=headphones']

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8',
            'Accept-Language': 'en',
            'Referer': 'https://www.amazon.com/',
        }
    }

    def parse(self, response):
        # Extract details of headphones
        headphones = response.xpath('//div[@data-component-type="s-search-result"]')
        
        if not headphones:
            self.logger.info('No headphones found on the page.')
            return

        for headphone in headphones:
            description = headphone.xpath('.//h2/a/span/text()').get()
            price = headphone.xpath('.//span[@class="a-price"]/span[@class="a-offscreen"]/text()').get()
            rating = headphone.xpath('.//span[@class="a-icon-alt"]/text()').get()
            product_url = response.urljoin(headphone.xpath('.//h2/a/@href').get())
            yield scrapy.Request(product_url, callback=self.parse_product, meta={'description': description, 'price': price, 'rating': rating})

    def parse_product(self, response):
        items=MyScrapyProjectItem()
        description= response.meta.get("description")
        price= response.meta.get("price")
        rating= response.meta.get("rating")

        brand = response.xpath("(//span[@class='a-size-base po-break-word'])[1]/text()").get()
        Model_name = response.xpath("(//span[@class='a-size-base po-break-word'])[2]/text()").get()
        color = response.xpath("(//span[@class='a-size-base po-break-word'])[3]/text()").get()
        form_factor = response.xpath("(//span[@class='a-size-base po-break-word'])[4]/text()").get()
        connectivity_Technology = response.xpath("(//span[@class='a-size-base po-break-word'])[5]/text()").get()
        
        items['description']=description
        items['price']=price
        items['rating']=rating
        items['brand']=brand
        items['Model_name']=Model_name
        items['color']=color
        items['form_factor']=form_factor
        items['connectivity_Technology']=connectivity_Technology
        


        yield {
            'description': response.meta['description'].strip() if response.meta['description'] else None,
            'price': response.meta['price'].strip() if response.meta['price'] else None,
            'rating': response.meta['rating'].strip() if response.meta['rating'] else None,
            'brand': brand.strip() if brand else None,
            'Model_name':Model_name if Model_name else None,
            'color': color.strip() if color else None,
            'form_factor':form_factor.strip() if form_factor else None,
            'connectivity_Technology' : connectivity_Technology.strip() if connectivity_Technology else None,
            

        }
        