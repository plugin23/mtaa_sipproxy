
#    Copyright 2014 Philippe THIRION
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#    https://github.com/tirfil/PySipFullProxy/blob/master/sipfullproxy.py

import sipfullproxy
import logging
import socketserver
import socket
import sys

def main():
    logger = sipfullproxy.initialize_logger("sipproxy")
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)

    if(len(sys.argv) == 2):
        ipaddress = sys.argv[1]

    logger.info(ipaddress)
    sipfullproxy.HOST = ipaddress
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (sipfullproxy.HOST, sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (sipfullproxy.HOST, sipfullproxy.PORT)
    server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()

main()