from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from queue import Queue

from bas.message import Message


server_input_queue = Queue()


class DevRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        data = {}

        paired_values = body.decode('utf-8').split('&')
        for pair in paired_values:
            key, value = pair.split('=')
            data[key] = value

        user = data.get('user')
        message = data.get('message')

        if user is not None and message is not None:
            message = Message(message, user)
            server_input_queue.put(message)
            print(server_input_queue)

        self.send_response(200)
        self.end_headers()
        return


class DevServer(Thread, HTTPServer):
    def __init__(self, host='localhost', port=9876):
        self.host = host
        self.port = port
        self.handler = DevRequestHandler
        HTTPServer.__init__(self, (self.host, self.port), self.handler)
        Thread.__init__(self)

    def start(self):
        print('Launching dev server...')
        super().start()

    def run(self):
        self.serve_forever()

    def stop(self):
        self.shutdown()
