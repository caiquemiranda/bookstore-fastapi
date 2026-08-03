from fastapi import FastAPI, HTTPException
import random, os, json

app = FastAPI()

BOOK_DATABASE = [
"book 1",
"book 2",
"book 3"
]

BOOKS_FILE = "books.json"

if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, 'r') as f:
        BOOK_DATABASE = json.load(f)

@app.get("/")
async def home():
    return "Welcome my bookstore"

@app.get("/list-books")
async def list_books():
    return {
        "books":BOOK_DATABASE
        }

@app.get("/list-book-by-index/{index}")
async def list_book_by_index(index: int):
    if index < 0 or index >= len(BOOK_DATABASE):
        raise HTTPException(404, "Index out of range")
    else:
        return {
            "books":BOOK_DATABASE[index]
            }

@app.get("/get-random-book")
async def get_random_book():
    return random.choice(BOOK_DATABASE)

@app.post("/add-book")
async def add_book(book: str):
    BOOK_DATABASE.append(book)
    with open(BOOKS_FILE, 'w') as f:
        json.dump(BOOK_DATABASE, f)
    return{
        "message":f'Book {book} was added.'
    }
    