from flask import Blueprint
from  pet.api import PetsApi    

pet_app = Blueprint('pet_app', __name__)

pet_app.add.add_url_rule('/pets/',view_function)