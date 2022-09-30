from typing import List
from pydantic import BaseModel


class Book(BaseModel):
    title: str
    category: str
    available_stock: int
    price: float
    num_stars: float
    upc_code: str
    image_url: str


class ResponseBooks(BaseModel):

    book_count: int
    categories: List[str]
    books: List[Book]
