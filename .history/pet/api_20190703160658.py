import json

from flask import abort, jsonify, request
from flask.views import MethodView


class PetsApi(MethodView):

    pets = [
        {"id":1, "name": u"Mac"},
        {"id":2, "name": u"Leo"},
        {"id":3, "name": u"Dave"}

    ]
    def get(self):
        return jsonify({"pets":self.pets})

    def post(self):
        if not request.json