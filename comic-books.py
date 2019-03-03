from bottle import run, route, view, get, post, request
from itertools import count

#ver1.1

class Comic:
    
    _ids = count(0)
    
    def __init__(self, title, stock, desc):
        self.id = next(self._ids)
        self.title = title
        self.stock = stock
        self.desc = desc
        
        

