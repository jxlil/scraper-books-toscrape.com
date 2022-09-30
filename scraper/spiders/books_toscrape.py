from scraper.items import BookLoader, BookItem
from scrapy import Spider


class BooksToscrapeSpider(Spider):
    name = "books-toscrape"
    allowed_domains = ["books.toscrape.com"]
    start_urls = [
        "http://books.toscrape.com/catalogue/category/books/biography_36/index.html",  # Biography
        "http://books.toscrape.com/catalogue/category/books/default_15/index.html",  # Default
    ]

    def parse(self, response):
        book_page_links = response.css(".product_pod a")
        yield from response.follow_all(book_page_links, self.parse_book)

        next_page_link = response.css(".next a::attr(href)").get()
        if next_page_link is not None:
            yield response.follow(next_page_link, self.parse)

    def parse_book(self, response):

        book = BookLoader(item=BookItem(), selector=response)
        book.add_css("title", css="h1::text")
        book.add_css("category", css=".breadcrumb li~ li+ li a::text")
        book.add_css("available_stock", css="tr:nth-child(6) td::text", re=r"([0-9]+)")
        book.add_css("price", css=".product_main .price_color", re=r"([0-9\.]+)")
        book.add_css("num_stars", css=".product_main .star-rating::attr('class')")
        book.add_css("upc_code", css="tr:nth-child(1) td::text")
        book.add_css("image_url", css="#product_gallery img::attr('src')")

        yield book.load_item()
