import requests

class OpenLibraryApi:
    BASE_URL = "https://openlibrary.org/isbn/"

    def search_by_isbn(self, isbn: str ) -> dict:
        response = requests.get(f"{self.BASE_URL}{isbn}.json")
        return response.json()