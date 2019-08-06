import os
import json
import falcon
from wsgiref import simple_server

from api.models import (
    Index
)

class Api:
    def __init__(self):
        try:
            api = falcon.API()
            api.add_route('/', Index())
            http = simple_server.make_server('0.0.0.0', 8080, api)
            try:
                http.serve_forever()
            except:
                http.shutdown()
        except Exception as e:
            print ('[Error Api-__init__]: {0}'.format(e))
