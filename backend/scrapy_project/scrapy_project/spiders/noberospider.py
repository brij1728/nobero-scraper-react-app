import scrapy

class NoberoSpider(scrapy.Spider):
    name = "noberospider"
    allowed_domains = ["nobero.com"]
    start_urls = ["https://nobero.com/pages/men"]
    handle_httpstatus_list = [302]  # Handle 302 redirects manually if needed

    def parse(self, response):
        # Check for redirects and log a warning if a 302 occurs
        if response.status == 302:
            self.logger.warning(f"Redirected to: {response.headers.get('Location')}")
            return

        # Find products on the page
        products = response.css('div.image-container')
        if not products:
            self.logger.warning("No products found on the page")
            return
        
        # Extract details from each product
        for product in products:
            # Extract image URL and handle missing values
            image_url = product.css('figure img::attr(src)').get()
            if image_url:
                image_url = response.urljoin(image_url)
            else:
                self.logger.warning("No image URL found for product")
            
            # Extract the title and handle missing values
            title = product.css('section.product-info h3::text').get()
            if not title:
                self.logger.warning("No title found for product")
                title = "No Title"
            
            # Extract the price and handle missing values
            price = product.css('article#price__regular::text').get()
            if not price:
                self.logger.warning(f"No price found for product: {title}")
                price = "No Price"

            # Yield the product details
            yield {
                'title': title.strip(),
                'image_url': image_url,
                'price': price.strip(),
            }

        # Follow pagination links if available
        next_page = response.css('a.pagination-next::attr(href)').get()
        if next_page:
            self.logger.info(f"Following pagination to next page: {next_page}")
            yield response.follow(next_page, self.parse)
        else:
            self.logger.info("No more pages to follow")
