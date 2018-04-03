
import logging
import selectors
import socket
import time
import os

HOST = 'localhost'
PORT = 40404

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')


class SelectorServer:
    def __init__(self, host, port):
        # Create the main socket that accepts incoming connections and start
        # listening. The socket is nonblocking.
        self.main_socket = socket.socket()
        self.main_socket.bind((host, port))
        self.main_socket.listen(100)
        self.main_socket.setblocking(False)

        # Create the selector object that will dispatch events. Register
        # interest in read events, that include incoming connections.
        # The handler method is passed in data so we can fetch it in
        # serve_forever.
        self.selector = selectors.DefaultSelector()
        self.selector.register(fileobj=self.main_socket,
                               events=selectors.EVENT_READ,
                               data=self.on_accept)

        # Keeps track of the peers currently connected. Maps socket fd to
        # peer name.
        self.current_peers = {}

    def on_accept(self, sock, mask):
        # This is a handler for the main_socket which is now listening, so we
        # know it's ready to accept a new connection.
        conn, addr = self.main_socket.accept()
        logging.info('accepted connection from {0}'.format(addr))
        conn.setblocking(False)
        self.flag = False

        self.current_peers[conn.fileno()] = conn.getpeername()
        # Register interest in read events on the new socket, dispatching to
        # self.on_read
        self.selector.register(fileobj=conn, events=selectors.EVENT_READ,
                               data=self.on_read)

    def close_connection(self, conn):
        # We can't ask conn for getpeername() here, because the peer may no
        # longer exist (hung up); instead we use our own mapping of socket
        # fds to peer names - our socket fd is still open.
        peername = self.current_peers[conn.fileno()]
        logging.info('closing connection to {0}'.format(peername))
        del self.current_peers[conn.fileno()]
        self.selector.unregister(conn)
        conn.close()

    def on_read(self, conn, mask):
        # This is a handler for peer sockets - it's called when there's new
        # data.
        try:
            data = conn.recv(1000)
            if self.flag == False:
                if data:
                    peername = conn.getpeername()
                    logging.info('got data from {}: {!r}'.format(peername, data))
                    action_dict  = eval(data)
                    if hasattr(self,action_dict['action']):
                        self.flag = True
                        func = getattr(self,action_dict['action'])
                        func(conn,mask)

                    else:
                        print('no func')
            else:
                print('flag True')
        except ConnectionResetError:
            self.close_connection(conn)

    def get(self,conn,mask):
        with open('1.log','rb')as f:
            if self.flag == True:
                for i in f:
                    conn.send(i)
                    conn.recv(1024)
                    # except BlockingIOError:
                    #     conn.close()
                    #     self.selector.unregister(conn)
                    #     self.selector.register(fileobj=conn, events=selectors.EVENT_READ,data=self.on_read)


    # def put(self,conn,mask):
    #     filesize = os.stat('150.img').st_size
    #
    #     with open('150.img.new','wb')as f:
    #         tmp_size = 0
    #         while tmp_size < filesize:
    #             tmp_file = conn.recv(1024)
    #             tmp_size += len(tmp_file)
    #             f.write(tmp_file)
    #
    #         else:
    #             self.selector.unregister(conn)
    #             self.close_connection(conn)


    def serve_forever(self):
        last_report_time = time.time()

        while True:
            # Wait until some registered socket becomes ready. This will block
            # for 200 ms.
            events = self.selector.select(timeout=0.2)

            # For each new event, dispatch to its handler
            for key, mask in events:
                handler = key.data
                handler(key.fileobj, mask)

            # This part happens roughly every second.
            cur_time = time.time()
            if cur_time - last_report_time > 1:
                logging.info('Running report...')
                logging.info('Num active peers = {0}'.format(
                    len(self.current_peers)))
                last_report_time = cur_time


if __name__ == '__main__':
    logging.info('starting')
    server = SelectorServer(host='127.0.0.1', port=9999)
    server.serve_forever()