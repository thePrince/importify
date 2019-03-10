from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

HOST_NAME = 'localhost'
PORT_NUMBER=3333

#simple local server set up to receive spotify authorization redirect.  
#code param is exchanged for an auth token, handled by Spotipy
#this just needs to be done once per username; spotipy caches the auth/refresh tokens
class AuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print('the authServer is serving a get request')
        params = urlparse(self.path).query
        print(params)
        self.wfile.close()


if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), AuthHandler)
    try:
        print('starting up auth server')
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('server shutting down')