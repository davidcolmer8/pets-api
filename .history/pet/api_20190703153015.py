from flask.views import MethodView
from flask import jsonify, request, abort

class pets(MethodView):

    pets = [
        {"id1":1, "name": u"Mac"},
        {"id2"}

    ]