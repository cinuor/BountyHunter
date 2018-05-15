# -*- coding: utf-8 -*-

from app import create_app
from config import config
from app.models import db


if __name__ == '__main__':
    
    myapp = create_app("default", config)
    with myapp.app_context():
        db.init_app(myapp)
        #db.drop_all()
        db.create_all()

    myapp.run(host='0.0.0.0', port=5000)
