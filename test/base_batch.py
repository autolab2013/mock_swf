# -*- coding utf-8 -*-
from multiprocessing import Process
import socket
import json

from mock_swf.swf_server import HOST, PORT

class BatchBase(object):
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def job(self, *args, **kwargs):
        raise Exception('job not implemented')

    def start_proc_with_target(self, target, *args, **kwargs):
        p = Process(target=target, args=args, kwargs=kwargs)
        p.start()
        p.join()

    def quest_server(self, quest):
        try:
            self.socket.connect((HOST, PORT))
            self.socket.send(json.dumps(quest))
            resp = json.loads(self.socket.recv(1024))
            return resp
        finally:
            self.socket.close()

    def run(self):
        self.start_proc_with_target(self.job, *args, **kwargs)


