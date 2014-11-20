"""Data structures  for the application.


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

import uuid
import subprocess
from threading import Thread

try:
    import json
except ImportError:
    import simplejson as json


def to_json(obj):
    # Defaults for consistent output
    kwargs = {'indent': 4,
              'separators': (',', ': ')
              }
    return json.dumps(obj, **kwargs)


class Payload(Thread):
    
    def __init__(self, cmd, params):
        Thread.__init__(self)
        self.uuid = uuid.uuid4().hex
        self.cmd = cmd
        self.params = params
        self.status = "pending"

    def __repr__(self):
        return "[%s]" % (self.uuid)

    def run(self):
        try:
            p = subprocess.Popen([self.cmd] + self.params,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        except OSError:
            self.status = "error:start('%s':No such file or directory" % self.cmd
            return
        self.status = "working"
        (out, err) = p.communicate()
        
        if err:
            self.status = "error:start (%s)" % err
        else:
            self.status = "finished"

    def get_id(self):
        return self.uuid

    def serialize(self):
        return { "id" : self.uuid,
                 "cmd" : self.cmd,
                 "params" : self.params,
                 "status" : self.status
               }

    def to_json(self):
        return to_json(self.serialize())


class Workflow(object):
    
    def __init__(self):
        self._id = uuid.uuid4()
        
        self.workflows = []
        #wf id, params, url

class Store(object):

    def __init__(self):
        self.store = {}


    def get(self, id):
        return self.store.get(id, None)


    def get_all(self):
        res = []
        for p_id in self.store:
            res.append(self.store[p_id].serialize())
        return to_json(res)


    def add(self, payload):
        if self.store.has_key(payload.get_id()):
            # Id already exists
            return None
        else:
            self.store[payload.get_id()] = payload
            payload.start()
            return payload

    def update(self, p):
        pass
        
