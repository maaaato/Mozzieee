# -*- coding: utf-8 -*-
from bottle import route, run, template

@route('/hello')
def hello():

    return template("Hello {{string}}",
                    string='World')


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080,
        debug=True, reloader=True)
    
        
