from collections import namedtuple, defaultdict, Counter, deque, OrderedDict

Book = namedtuple("Book", "id title author genre copies")
books = OrderedDict()
by_genre = defaultdict(list)
borrow_count = Counter()
genre_count = Counter()
waiting = defaultdict(deque)

def add_book(i, t, a, g, c):
    books[i] = Book(i, t, a, g, c)
    by_genre[g].append(i)

def borrow_book(i, u):
    b = books[i]
    if b.copies > 0:
        books[i] = b._replace(copies=b.copies - 1)
        borrow_count[i] += 1; genre_count[b.genre] += 1
        print(f"{u} borrowed {b.title}")
    else:
        waiting[i].append(u); print(f"{u} waitlisted for {b.title}")

def return_book(i, u):
    b = books[i]
    if waiting[i]:
        nxt = waiting[i].popleft()
        borrow_count[i] += 1; genre_count[b.genre] += 1
        print(f"{u} returned {b.title}, given to {nxt}")
    else:
        books[i] = b._replace(copies=b.copies + 1)
        print(f"{u} returned {b.title}")

def display_by_genre(g):
    for i in by_genre[g]: print(books[i])

def show_waiting_list(i):
    print(list(waiting[i]) or "No waiting list")

def display_top_books():
    print("Top books:", borrow_count)
    print("Top genres:", genre_count)
add_book(1, "Gatsby", "Fitzgerald", "Classic", 1)
borrow_book(1, "Alice")
borrow_book(1, "Bob")
return_book(1, "Alice")
display_by_genre("Classic")
show_waiting_list(1)
display_top_books()


