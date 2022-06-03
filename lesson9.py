class Books:
    def __init__(self, name, author, page):
        self.name = name
        self.author = author
        self.page = page

    @staticmethod
    def good_book():
        print("it's a good book")

    @classmethod
    def type_of_book(cls, name, author, page):
        return cls(name, author, page)


book1 = Books("overnight in lisbon", 'remark', 314)

print(book1.name)
book1.good_book()
