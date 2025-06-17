from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import random
import time

PORT = 8888

class MySimpleHTTPRequestHandler(SimpleHTTPRequestHandler):
    
    def end_headers(self):
        self.send_header("Content-Security-Policy", "frame-ancestors 'self'")
        super().end_headers()

    def do_GET(self):
        if self.path == "/api/data":
            # Generate random data
            response = [
                {"ID": i, "Name": f"Item {random.randint(1, 1000)}", "Value": random.randint(1, 1000)}
                for i in range(1, 101)
            ]

            time.sleep(2) # クライアントでスピナー表示したいため敢えて遅延

            # Send response
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            # Default behavior for other paths
            super().do_GET()

if __name__ == "__main__":
    # Define the server address and port
    server_address = ("", PORT)

    # Create an instance of the HTTP server with the specified address and request handler
    httpd = HTTPServer(server_address, MySimpleHTTPRequestHandler)

    print(f"http://localhost:{PORT}")

    # Start the server
    httpd.serve_forever()
