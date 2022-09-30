# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from itemloaders.processors import TakeFirst, MapCompose, Join
from itemloaders import ItemLoader
from scrapy import Field, Item


class BookLoader(ItemLoader):
    default_output_processor = TakeFirst()

    title_in = MapCompose(str.strip)
    title_out = Join()

    def price_out(self, values: list) -> float:

        return float(values[0])

    def num_stars_out(self, values: list) -> float:

        nums = ["One", "Two", "Three", "Four", "Five"]
        value = values[0].split(" ")[-1]
        return float(nums.index(value) + 1)

    def image_url_out(self, values: list) -> str:

        value = values[0]
        return value.replace("../../", "http://books.toscrape.com/")

    def available_stock_out(self, values: list) -> int:

        value = values[0]
        return int(value)


class BookItem(Item):

    title = Field()
    category = Field()
    available_stock = Field()
    price = Field()
    num_stars = Field()
    upc_code = Field()
    image_url = Field()
