import sipfullproxy
import logging
import socketserver
import socket

def main():
    logger = sipfullproxy.initialize_logger("sipproxy")
    hostname = socket.gethostname()
    #logger.info(hostname)
    ipaddress = socket.gethostbyname(hostname)
    #logger.info(ipaddress)

    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, sipfullproxy.PORT)
    server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()

main()