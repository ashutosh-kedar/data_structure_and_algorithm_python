from contextlib import contextmanager


@contextmanager
def connect(url):
    print('connection established:',url)
    try:
        yield 'connection_obj'
    finally:
        print('closing connection:',url)




with connect('book.txt') as connect_obj:
    print('Using connection object:',connect_obj)

