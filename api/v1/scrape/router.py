from scraper.spiders.books_toscrape import BooksToScrapeSpider
from scrapy.utils.project import get_project_settings

from scrapyscript import Job, Processor
from fastapi import APIRouter

from .models import ResponseBooks

router = APIRouter(prefix="/v1/scrape", tags=["Scrape"])
processor = Processor(settings=get_project_settings())


@router.get("/")
async def check():
    return {"status": "running"}


@router.get("/books", response_model=ResponseBooks)
async def scrape_books():

    job = Job(BooksToScrapeSpider)
    data = processor.run(job)

    response = ResponseBooks(
        books=data,
        book_count=len(data),
        categories=list({book["category"] for book in data}),
    )

    return response
