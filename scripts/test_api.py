import requests

def get_book_by_olid(book_olid: str) -> dict | None:
    base_url_olid = f"https://openlibrary.org/{book_olid}.json"
    response = requests.get(base_url_olid)

    if response.status_code != 200:
        return None

    return response.json()

def get_book_by_isbn(isbn: str) -> dict | None:
    base_url_isbn = f"https://openlibrary.org/isbn/{isbn}.json"
    response = requests.get(base_url_isbn)

    if response.status_code != 200:
        return None

    return response.json()

def filter_by_language(docs: list, language_code: str) -> list:
    return [
        doc for doc in docs
        if language_code in doc.get("languages", [])
    ]

if __name__ == '__main__':
    result_by_isbn = get_book_by_isbn('9783423432832')
    print(result_by_isbn)
    result_book_olid = result_by_isbn['key']
    print(result_book_olid)
    result_by_book_olid = get_book_by_olid(result_book_olid)
    print(result_by_book_olid)

    if result_by_book_olid:
        print(result_by_book_olid['title'])
        if result_by_book_olid.get('isbn_13'):
            print(result_by_book_olid['isbn_13'])
        else:
            print("Kein ISBN 13")
        if result_by_book_olid.get('isbn_10'):
            print(result_by_book_olid['isbn_10'])
        else:
            print("Kein ISBN 10")
        if result_by_book_olid.get('publishers'):
            print(result_by_book_olid['publishers'])
        else:
            print("Kein publisher")
        if result_by_book_olid.get('description'):
            print(result_by_book_olid['description']['value'])
        else:
            print("Kein description")
        if result_by_book_olid.get('publish_date'):
            print(result_by_book_olid['publish_date'])
        else:
            print("Kein publish_date")
        if result_by_book_olid.get('covers'):
            print(result_by_book_olid['covers'])
        else:
            print("Kein covers")