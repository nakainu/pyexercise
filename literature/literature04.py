from datetime import datetime


def output_books(books, only_kindle):
    for book in sorted(books, key=lambda x: x['published_at'], reverse=True):
        if only_kindle == 1 and book['category'] != 'Kindle':
            # only_kindle=1かつ'Kindle'ではない時は先頭に戻る
            # only_kindle=1かつ'kindle'である時は処理が進む
            continue
        print(f"出版日: {book['published_at']}")
        print(f"書籍名: {book['title']}")
        print(f"金額: {book['price']}")
        print("----------")



books = []
with open('wrong_books.csv', encoding='utf-8') as csv:
    for row in csv:
        col = row.split(',')
        book = {}
        book['published_at'] = datetime.strptime(col[0], "%Y/%m/%d")
        book['category'] = col[1].replace('[', '').replace(']', '')
        book['title'] = col[2]
        book['author'] = col[3]
        try:
            book['price'] = int(col[4])
        except ValueError:
            price = 0
            book['price'] = price
        books.append(book)

output_books(books, 0)
