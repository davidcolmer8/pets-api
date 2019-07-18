from flask.views import MethodView
from flask import jsonify, request, abort

class pets(MethodView):

    pets = [
        {"id":1, "name": u"Mac"},
        {"id":2, "name": u"Leo"},
        {"id":3, "name": u"Dave"}

    ]
    def get