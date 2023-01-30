from http.server import SimpleHTTPRequestHandler, HTTPServer
import socketserver
import io


class RequestHandler(SimpleHTTPRequestHandler):
	def do_POST(self):
		r, info = self.deal_post_data()
		f = io.BytesIO()
		f.write(b"blah")
		print(r, info, "by: ", self.client_address)
		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.send_header("Content-Length", str(length))
		self.end_headers()
		





def run():
	serverAddress = ('', 80)
	with socketserver.TCPServer(serverAddress, RequestHandler) as httpd:
		print("started at port 80")
		httpd.serve_forever()

run()