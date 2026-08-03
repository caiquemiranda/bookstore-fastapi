from fastapi import FastAPI

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
async def list-books():
    return {
        books:BOOK_LIST

}
