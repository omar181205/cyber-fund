from http.server import BaseHTTPRequestHandler, HTTPServer

class SpyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        secret_data = self.rfile.read(content_length)
        
        with open("received_spy_file.enc", 'wb') as f:
            f.write(secret_data)
        
        self.send_response(200)
        self.end_headers()
        print(" Secret file received!")

print("Starting spy server on port 8080...")
httpd = HTTPServer(('localhost', 8080), SpyServer)
httpd.serve_forever()