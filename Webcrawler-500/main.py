from socket import socket


def fetch(url):
    sock = socket()
    sock.connect(("xkcd.com", 80))
    request = "GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n".format(url)
    requestascii = request.encode("ascii")
    return requestascii
