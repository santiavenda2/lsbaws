import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.join(CURRENT_DIR, 'helloworld'))
from helloworld import wsgi


app = wsgi.application
