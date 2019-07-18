import os
import sys
from os import path
from xmlrpc.client import Server

from flask_script import Manager, Server

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from application