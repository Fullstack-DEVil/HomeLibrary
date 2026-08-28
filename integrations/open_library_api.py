import requests

class OpenLibraryApi:
    BASE_URL_ISBN = "https://openlibrary.org/isbn/"
    BASE_URL_OLID = "https://openlibrary.org/"

    def search_by_isbn(self, isbn: str ) -> dict:
        response = requests.get(f"{self.BASE_URL_ISBN}{isbn}.json")
        return response.json()

    def get_book_details_by_olid(self, olid: str) -> dict:
        response = requests.get(f"{self.BASE_URL_OLID}{olid}.json")
        return response.json()
