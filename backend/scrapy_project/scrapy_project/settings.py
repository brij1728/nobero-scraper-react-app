# Project name and spider settings
BOT_NAME = "scrapy_project"

SPIDER_MODULES = ["scrapy_project.spiders"]
NEWSPIDER_MODULE = "scrapy_project.spiders"

# Disable robots.txt rules for more flexibility in crawling
ROBOTSTXT_OBEY = False

# Set a browser-like User-Agent to mimic real user behavior and avoid blocks
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Disable redirects to avoid being redirected to invalid pages
REDIRECT_ENABLED = False

# Download delay to avoid being blocked (adjust as needed)
DOWNLOAD_DELAY = 1

# Handle SSL/TLS verification issues by forcing a specific method and disabling verification
DOWNLOADER_CLIENT_TLS_METHOD = 'TLSv1.2'
DOWNLOADER_CLIENT_TLS_VERIFY = False

# Enable extensive logging for debugging purposes (set to DEBUG during development)
LOG_LEVEL = 'DEBUG'

# Future-proof settings for request fingerprinting and reactor
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Splash server URL for rendering JavaScript-heavy pages
SPLASH_URL = 'http://localhost:8050'

# Splash downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
}

# Splash spider middlewares
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Use Splash-aware dupe filter and cache storage to handle duplicates and caching effectively
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# Optional: Enable caching to speed up repetitive requests (adjust expiration as needed)
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0  # Set to 0 to disable expiration
# HTTPCACHE_DIR = 'httpcache'

# Optional: Enable AutoThrottle to regulate the request rate dynamically
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# AUTOTHROTTLE_DEBUG = False
