from flask import Blueprint
from pet.api import PetsApi    

pet_app = Blueprint('pet_app', __name__)

pet_app.add_url_rule('/pets/',view_func=PetsApi.as_view('pets'))

PetsApi.as_v