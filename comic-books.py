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
    Comic("Water Woman","3","0"),
    Comic("Lizard Man","12","0"),
    Comic("Super Dude","8","0"),
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


run(host='0.0.0.0', port = 8080, reloader = True, debug = True)

        
        
        

