from fastapi import APIRouter

router = APIRouter(prefix="/scrape", tags=["Scrape"])


@router.get("/books")
def scrape_books():
    return {}
