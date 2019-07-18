from flask import Blueprint
from  pet.api import PetsApi    

pet_app = Blueprint('pet_app', __name__)