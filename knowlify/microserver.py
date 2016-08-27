import SimpleHTTPServer
import SocketServer
import config


def start_server(port=config.MPORT, data_dir=config.DATA_DIR):
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer((data_dir, port), Handler)
    httpd.serve_forever()
    return httpd, Handler


def close_server(socket_server):
    assert isinstance(socket_server, SocketServer.TCPServer)
    socket_server.server_close()