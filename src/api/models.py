import json

class Index:
    def on_get(self, req, res):
        index_file = open('./views/index.html', 'r')
        print (index_file)
        resolve_response(res, {
            'status': '200 OK',
            'body': index_file.read(),
            'content_type': 'text/html; charset=UTF-8'
        })

def resolve_response(res, attributes):
    res.status       = attributes.get('status', '200 OK')
    res.body         = attributes.get('body', None)
    res.content_type = attributes.get('content_type', 'application/json')
