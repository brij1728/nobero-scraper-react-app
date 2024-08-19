import scrapy

class NoberoSpider(scrapy.Spider):
    name = "noberospider"
    allowed_domains = ["nobero.com"]
    start_urls = ["https://nobero.com/pages/men"]

    def parse(self, response):
        # Example: Extract product URLs and follow them
        product_links = response.css('div.product-card a::attr(href)').getall()
        for link in product_links:
            yield response.follow(link, self.parse_product)

    def parse_product(self, response):
        # Extract product details
        yield {
            'title': response.css('h1.product-title::text').get(),
            'price': response.css('span.price::text').get(),
            'category': response.css('div.breadcrumb-item::text').get(),
            # Add other fields as needed, like SKU, sizes, colors, etc.
        }
