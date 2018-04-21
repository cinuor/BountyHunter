# -*- coding: utf-8 -*-
#import sys, os
#print(os.path.abspath(__file__))
#print(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from config import config


if __name__ == '__main__':
    
    myapp = create_app("default", config)

    myapp.run()
