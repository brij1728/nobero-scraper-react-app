# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import Response, Request
from scrapy.exceptions import IgnoreRequest

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class ScrapyProjectSpiderMiddleware:
    """
    Spider middleware is responsible for processing the spider input/output.
    """

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        """
        Called for each response that goes through the spider middleware
        and into the spider.
        :param response: Response object
        :param spider: The spider instance
        :return: None or raise an exception
        """
        # Example: You can perform additional checks or processing on the response here.
        return None

    def process_spider_output(self, response, result, spider):
        """
        Called with the results returned from the Spider after
        it has processed the response.
        :param response: Response object
        :param result: The output from the spider (could be items or more requests)
        :param spider: The spider instance
        :return: Iterable of Request, or item objects
        """
        for item in result:
            yield item

    def process_spider_exception(self, response, exception, spider):
        """
        Called when an exception is raised while processing the response in the spider.
        :param response: Response object
        :param exception: The exception raised
        :param spider: The spider instance
        :return: None or an iterable of Request or item objects.
        """
        spider.logger.error(f"Exception occurred: {exception}")
        pass

    def process_start_requests(self, start_requests, spider):
        """
        Called with the start requests of the spider before they are processed.
        :param start_requests: The initial requests from the spider
        :param spider: The spider instance
        :return: Iterable of Request objects
        """
        for request in start_requests:
            yield request

    def spider_opened(self, spider):
        """
        Called when the spider is opened.
        :param spider: The spider instance
        """
        spider.logger.info(f"Spider opened: {spider.name}")


class ScrapyProjectDownloaderMiddleware:
    """
    Downloader middleware is responsible for processing the requests and responses
    between the spider and the downloader.
    """

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """
        Called for each request that goes through the downloader middleware.
        :param request: The request object
        :param spider: The spider instance
        :return: None, Response object, or raise IgnoreRequest
        """
        # Example: Modify request headers here or log the request
        spider.logger.info(f"Processing request: {request.url}")
        return None

    def process_response(self, request, response, spider):
        """
        Called with the response returned from the downloader.
        :param request: The request object
        :param response: The response object
        :param spider: The spider instance
        :return: Response object or raise IgnoreRequest
        """
        # Example: Check for specific status codes and raise IgnoreRequest
        if response.status == 404:
            spider.logger.warning(f"404 error encountered at: {request.url}")
            raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        """
        Called when a download handler or process_request raises an exception.
        :param request: The request object
        :param exception: The exception raised
        :param spider: The spider instance
        :return: None or Response object
        """
        spider.logger.error(f"Exception occurred for {request.url}: {exception}")
        return None  # Returning None will continue processing this exception

    def spider_opened(self, spider):
        """
        Called when the spider is opened.
        :param spider: The spider instance
        """
        spider.logger.info(f"Spider opened: {spider.name}")
