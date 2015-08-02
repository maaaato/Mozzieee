# -*- coding: utf-8 -*-
from bottle import route, run, template

@route('/photo/<image_path:path>')
def photo(image_path):
    return template('image_path={{image_path}}',
                    image_path=image_path)

@route('/greeting/<name>')
def greeting(name):
    return template('Hello {{name}}.',
                    name=name)

@route('/hello')
def hello():

    return template("Hello {{string}}",
                    string='World')


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080,
        debug=True, reloader=True)
    
        
