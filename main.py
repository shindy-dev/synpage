from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8888

if __name__ == "__main__":
    # Define the server address and port
    server_address = ("", PORT)

    # Create an instance of the HTTP server with the specified address and request handler
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    print(f"http://localhost:{PORT}")

    # Start the server
    httpd.serve_forever()
