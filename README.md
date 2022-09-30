
# scraper-books-toscrape.com
scraper for the website books.toscrape.com

## Installation

### pre-requisites

| Concept                                         | Version  |
|-------------------------------------------------|----------|
| [Docker](https://docs.docker.com/get-docker/)   | 20.10    |
| [Git](https://git-scm.com/downloads)            |  2.37    |


### install

1. Clone this repository

```bash
git clone https://github.com/jxlil/scraper-books-toscrape.com.git
cd scraper-books-toscrape.com
```

2. Deploy scraper with `docker compose`

```bash
docker compose up -d
```

3. Check scraper status

```bash
curl http://0.0.0.0:3000/v1/scrape/
# expected output: {"status":"running"}
```

## Use

Now you can run this scraper to get all the books in the categories:

- [Biography](http://books.toscrape.com/catalogue/category/books/biography_36/index.html)
- [Default](http://books.toscrape.com/catalogue/category/books/default_15/index.html)

To run the scraper you can do the following request:

```bash
curl --silent http://0.0.0.0:3000/v1/scrape/books
```

In the `exports/` directory you will find a `JSON` and `CSV` file with the results.

---

You can also use [jq](https://stedolan.github.io/jq/download/) and save the result in `JSON` format in any file

```bash
curl --silent http://0.0.0.0:3000/v1/scrape/books | jq . > books.json
```

#### example output:
```json
{
  "book_count": 1,
  "categories": [
    "Biography",
  ],
  "books": [
    {
      "title": "The Rise of Theodore Roosevelt (Theodore Roosevelt #1)",
      "category": "Biography",
      "available_stock": 3,
      "price": 42.57,
      "num_stars": 3,
      "upc_code": "1a5044d233936b1a",
      "image_url": "http://books.toscrape.com/media/cache/4c/09/4c090b85892f532210e44d84b752b64d.jpg"
    }
  ]
}
```
