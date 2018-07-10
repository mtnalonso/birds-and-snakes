from threading import Thread
from queue import Queue
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from bas.message import Message


server_input_queue = Queue()


class DevRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        data = json.loads(body)

        message = Message(data.get('message'), data.get('user'))
        server_input_queue.put(message)

        self.send_response(200)
        self.end_headers()
        return
    
    def log_message(self, format, *args):
        return


class DevServer(Thread, HTTPServer):
    def __init__(self, host='localhost', port=9876):
        self.host = host
        self.port = port
        self.handler = DevRequestHandler
        HTTPServer.__init__(self, (self.host, self.port), self.handler)
        Thread.__init__(self)

    def start(self):
        super().start()

    def run(self):
        self.serve_forever()

    def stop(self):
        self.shutdown()
