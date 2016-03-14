#!/usr/bin/env python
"""Static file server, using Python's CherryPy"""
import cherrypy
from cherrypy.lib.static import serve_file

import os.path

class Root:
    @cherrypy.expose
    def index(self, name):
        return serve_file(os.path.join(static_dir, name))

if __name__=='__main__':
    static_dir = os.path.abspath(os.getcwd())
    print "\nstatic_dir: %s\n" % static_dir

    cherrypy.config.update( {  #mconfiguring the server here
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 8001,
        } )
    conf = {
        '/': {  
            'tools.staticdir.on':   True,  
            'tools.staticdir.root': static_dir,
            'tools.staticdir.dir':  '',
        }
    }

    cherrypy.quickstart(Root(), '/', config=conf)