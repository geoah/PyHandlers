"""WSGI application to manage payloads.

Copyright 2014 University of Liverpool

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from webob import Request, Response
try:
    import json
except ImportError:
    import simplejson as json

from data import Store, Payload



class WSGIPayloads(object):
    
    def __init__(self):
        self.store = Store()

    def _setUp(self, environ):
        # Prepare application to handle a new request
        # Wrap environ in a Request object
        self.request = Request(environ, charset='utf8')
        # Create a Response object with defaults for status, encoding etc.
        # Methods should over-ride these defaults as necessary
        self.response = Response()

    def __call__(self, environ, start_response):
        self._setUp(environ)
        
        if self.request.method == "GET":
            if self.request.path_info.find('/') != -1:
                uuid = self.request.path_info.split('/')[1]
                payload = self.store.get(uuid)
                if payload:
                    self.response.status = "200 ok"
                    self.response.body = payload.to_json()
                else:
                    self.response.status = "404 Not Found"
            else:
                self.response.status = "200 ok"
                self.response.body = self.store.get_all()
        else:
            payload = self.add_payload()
            if payload:
                self.response.status = "201 created"
                self.response.body = payload.to_json()
        
        return self.response(environ, start_response)

    def add_payload(self):
        data = json.loads(self.request.body)
        payload = Payload(data['Cmd'],
                          data['Params'])
        try:
            self.store.add(payload)
        except:
            print "Erreur"
            return None
        return payload


