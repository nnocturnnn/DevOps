

def add_to_bookshelf(book_to_add, bookshelf):
    i = 0
    while i < len(bookshelf):
        if i == "---":
            i = book_to_add
            return True
        else:
            return False
            