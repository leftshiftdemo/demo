#!/usr/bin/env python

import bottle # Web server
from bottle import run, route, request


@route('/')
def index():
    """ Display welcome & instruction messages """
    return "<p>Welcome to my extra simple bottle.py powered server !</p> \
           <p>There are two ways to invoke the web service :\
           <ul><li>http://localhost:8080/up?s=type_your_string_here</li>\
           <li>http://localhost:8080/up?URL=http://url_to_file.txt</li></ul>"


if __name__ == '__main__':
    # To run the server, type-in $ python server.py
    bottle.debug(True) # display traceback 
    run(host='0.0.0.0', port=8080, reloader=True)
