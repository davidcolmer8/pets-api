from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app(**config):
