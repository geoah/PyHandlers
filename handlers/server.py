"""Handlers Demonstration Server.

Start a demonstration server, including a pure Python application
router.

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


from paste.urlmap import URLMap
import sys
from argparse import ArgumentParser
import paste.httpserver

from wsgi import WSGIPayloads


def configure_argparser():
    """Add commandline arguments"""
    argParser = ArgumentParser()
    # Set default hostname
    hostname = '127.0.0.1'
    argParser.add_argument('--hostname', type=str,
                           action='store', dest='hostname',
                           default=hostname, metavar='HOSTNAME',
                           help=("name of host to listen on. default"
                                )
                           )
    argParser.add_argument('-p', '--port', type=int,
                           action='store', dest='port',
                           default=8000, metavar='PORT',
                           help=("number of port to listen on. default: "
                                "%(default)s")
                          )
    return argParser


def get_application():
    """Create and return the root application for the server.

    :returns: WSGI callable
    :rtype: paste.urlmap.URLMap
    """
    # Mount various Apps and static directories
    urlmap = URLMap()
    urlmap['/payloads'] = WSGIPayloads()
    return urlmap


def main(argv=None):
    """Start up a simple app server to serve the application."""
    argparser = configure_argparser()
    application = get_application()
    if argv is None:
        args = argparser.parse_args()
    else:
        args = argparser.parse_args(argv)
    url = "http://{0}:{1}/payloads".format(args.hostname, args.port)
    
    print "You should be able to access the application at:"
    paste.httpserver.serve(application,
                           host=args.hostname,
                           port=args.port
                           )


if __name__ == "__main__":
    sys.exit(main())
