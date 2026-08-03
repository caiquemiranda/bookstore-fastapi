from fastapi import FastAPI, HTTPException
import random

app = FastAPI()

BOOK_LIST = [
"book 1",
"book 2",
"book 3"
]


@app.get("/")
async def home():
    return "Welcome my bookstore"

@app.get("/list-books")
async def list_books():
    return {
        "books":BOOK_LIST
}

@app.get("/list-book-by-index/{index}")
async def list_book_by_index(index: int):
    if index < 0 or index >= len(BOOK_LIST):
        raise HTTPException(404, "Index out of range")
    else:
        return {
            "books":BOOK_LIST[index]
}

@app.get("/get-random-book")
async def get_random_book():
    return random.choice(BOOK_LIST)


