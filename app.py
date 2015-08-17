# -*- coding: utf-8 -*-

from bottle import route, run, template, request
from bottle import static_file
from schedule import Aschedule
import datetime
import os

# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@route('/assets/css/<filename>')
def css_dir(filename):
    """ set css dir """
    return static_file(filename, root=BASE_DIR+"/views/assets/css/")

@route('/assets/js/<filename>')
def css_dir(filename):
    """ set css dir """
    return static_file(filename, root=BASE_DIR+"/views/assets/js/")

@route('/dist/<filename>')
def js_dir(filename):
    """ set js dir """
    return static_file(filename, root=BASE_DIR+"/views/dist/")

@route('/')
def index():
    aschedule = Aschedule("test")
    sd = aschedule.getSchedule()
    
    return template("index",
                    aschedule=sd,
                    request=request
    )


if __name__ == '__main__':
    
    run(host='0.0.0.0',
        port=8080,
        debug=True,
        reloader=True
    )
    
        
