# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime

import json
import csv


class JsonWriterPipeline:
    def open_spider(self, _):
        date = datetime.strftime(datetime.today(), "%y%m%d_%H%M%S")
        self.file = open(f"./exports/books-{date}.json", "w")
        self.data = list()

    def close_spider(self, _):
        self.file.write(json.dumps(self.data, indent=2))
        self.file.close()

    def process_item(self, item, _):
        self.data.append(dict(item))
        return item


class CsvWritePipeline:
    def open_spider(self, _):
        date = datetime.strftime(datetime.today(), "%y%m%d_%H%M%S")
        self.file = open(f"./exports/books-{date}.csv", "w")
        self.data = list()

    def close_spider(self, _):
        writer = csv.DictWriter(self.file, fieldnames=self.data[0].keys())
        writer.writeheader()
        writer.writerows(self.data)
        self.file.close()

    def process_item(self, item, _):
        self.data.append(dict(item))
        return item
