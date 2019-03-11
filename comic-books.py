from bottle import run, route, view, get, post, request
from itertools import count

#ver1.1

class Comic:
    
    _ids = count(0)
    
    def __init__(self, title, stock, sold):
        self.id = next(self._ids)
        self.title = title
        self.stock = stock
        self.sold = sold
        
        
comics = [
    Comic("Water Woman",3,0),
    Comic("Lizard Man",12,0),
    Comic("Super Dude",8,0),
]


#pages
#index page
@route('/')
@view('index')
def index():
    pass

#stock-levels page
@route('/stock-levels')
@view('stock-levels')
def stock_levels():
    data = dict (stock_list = comics)
    return data


#add sell-book-success


@route('/sell-book-success/<comic_id>')
@view('sell-book-success')
def sell_book_success(comic_id):
    comic_id = int(comic_id)
    found_book = None
    for comic in comics:
        if comic.id == comic_id:
            found_book = comic
    data = dict (comic = found_book)
    if found_book.stock == 0 or found_book.stock == "OUT OF STOCK":
        found_book.stock = ("OUT OF STOCK")
    else:
        found_book.stock = found_book.stock - 1
        found_book.sold = found_book.sold + 1
    return data









run(host='0.0.0.0', port = 8080, reloader = True, debug = True)

        
        
        

