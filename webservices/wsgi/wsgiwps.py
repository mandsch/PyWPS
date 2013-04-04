#!/usr/bin/env python

"""
PyWPS wsgi script

    SetHandler python-program
    PythonHandler wps
    PythonDebug On
    PythonPath "sys.path+['/usr/local/pywps-VERSION/']"
    PythonAutoReload On

for mod_wsgi:
    SetEnv PYWPS_CFG usr/local/wps/pywps.cfg
    SetEnv PYWPS_PROCESSES /usr/local/wps/processes/
    SetEnv PYTHONPATH "/usr/local/pywps-VERSION/"
    <Directory /srv/www/wsgi-scripts/>
        Order allow,deny
        Allow from all
    </Directory>
    WSGIScriptAlias /wpswsgi /srv/www/wsgi-scripts/wsgiwps.py

.. moduleauthor: Jachym Cepicky jachym bnhelp cz
"""

# Author:	Jachym Cepicky
#        	http://les-ejk.cz
# License:
#
# Web Processing Service implementation
# Copyright (C) 2006 Jachym Cepicky
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

import sys, os

import pywps
from pywps.Exceptions import *

def application(environ, start_response):

    status = '200 OK'
    response_headers = [('Content-type','text/xml')]
    start_response(status, response_headers)

    if "PYWPS_PROCESSES" in environ:
        os.environ["PYWPS_PROCESSES"] = environ["PYWPS_PROCESSES"]
    if "PYWPS_CFG" in environ:
        os.environ["PYWPS_CFG"] = environ["PYWPS_CFG"]

    inputQuery = None
    if "REQUEST_METHOD" in environ and environ["REQUEST_METHOD"] == "GET":
        inputQuery = environ["QUERY_STRING"]
    elif "wsgi.input" in environ:
        inputQuery = environ['wsgi.input']

    if not inputQuery:
        err =  NoApplicableCode("No query string found.")
        return [err.getResponse()]


    # create the WPS object
    try:
        wps = pywps.Pywps(environ["REQUEST_METHOD"])
        if wps.parseRequest(inputQuery):
            pywps.debug(wps.inputs)
            wps.performRequest()
            return wps.response
    except WPSException,e:
        return [e]
    except Exception, e:
        return [e]


if __name__ == '__main__':

    import os

    # import processes from the tests directory
    os.environ["PYWPS_PROCESSES"] =  os.path.join(
            os.path.split(
                os.path.dirname(
                    pywps.__file__
            )
        )[0],"tests","processes")

    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8081, application)
    srv.serve_forever()
