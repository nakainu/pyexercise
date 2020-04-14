from datetime import datetime

books = []
with open('books.csv', encoding='utf-8') as csv:
    for row in csv:
        col = row.split(',')
        book = {}
        book['published_at'] = datetime.strptime(col[0], "%Y/%m/%d")
        book['category'] = col[1].replace('[', '').replace(']', '')
        book['title'] = col[2]
        book['author'] = col[3]
        book['price'] = int(col[4].replace('\n', ''))
        books.append(book)

for book in sorted(books, key=lambda x: x['published_at'], reverse=True):
    print(f"出版日: {book['published_at']}")
    print(f"書籍名: {book['title']}")
    print("----------")
