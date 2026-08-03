from fastapi import FastAPI, HTTPException


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
