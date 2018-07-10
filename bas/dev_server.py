from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread


class DevRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        data = {}

        paired_values = body.decode('utf-8').split('&')
        for pair in paired_values:
            key, value = pair.split('=')
            data[key] = value

        self.send_response(200)
        self.end_headers()
        return


class DevServer(Thread, HTTPServer):
    def __init__(self, port, host='localhost', queue=None):
        self.host = host
        self.port = port
        self.queue = queue
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


if __name__ == '__main__':
    DevServer(9876).start()
