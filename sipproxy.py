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
        print(sys.argv[1])
        ipaddress = sys.argv[1]

    sipfullproxy.HOST = ipaddress
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (sipfullproxy.HOST, sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (sipfullproxy.HOST, sipfullproxy.PORT)
    server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()

main()