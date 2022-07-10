
import json
from pathlib import Path
from typing import Dict, List, Optional

from schemas import Book


class BookDAO:
    @staticmethod
    def _load_books() -> List[Dict]:
        Path("db.json").touch(exist_ok=True)
        with open("db.json", "r+") as f:
            content = f.read()
            if content:
                return json.loads(content)
            return []

    @staticmethod
    def _save_books(books: List[Dict]) -> None:
        with open("db.json", "r+") as f:
            f.seek(0)
            f.write(json.dumps(books))
            f.truncate()

    @staticmethod
    def create(book: Book) -> None:
        books = BookDAO._load_books()

        for b in books:
            if b["id"] == book.id:
                raise Exception("id already exists")

        books.append(book.dict())

        BookDAO._save_books(books)

    @staticmethod
    def get(book_id: int) -> Dict:
        books = BookDAO._load_books()

        for b in books:
            if b["id"] == book_id:
                return b

        raise Exception("book not found")

    @staticmethod
    def list() -> List[Dict]:
        return BookDAO._load_books()

    @staticmethod
    def update(book_id: int, name: Optional[str] = None, isbn: Optional[str] = None, quantity: Optional[int] = None) -> None:
        books = BookDAO._load_books()

        for i in range(len(books)):
            if books[i]["id"] == book_id:
                if name:
                    books[i]["name"] = name
                if isbn:
                    books[i]["isbn"] = isbn
                if quantity:
                    books[i]["quantity"] = quantity
                break
        BookDAO._save_books(books)

    @staticmethod
    def delete(book_id: int) -> None:
        books = BookDAO._load_books()

        for i in range(len(books)):
            if books[i]["id"] == book_id:
                books.pop(i)
                break

        BookDAO._save_books(books)
