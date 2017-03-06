# -*- coding utf-8 -*-
import json
import socket
import sys

from workflow import Workflow
from workflow_manager import WorkflowManager

HOST='localhost'
PORT=8888

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((HOST, PORT))
        sock.listen(10)
        conn, addr = sock.accept()
        print 'connected with {host}:{port}'.format(host=addr[0], port=addr[1])
        workflow_manager = WorkflowManager()
        test_workflow = Workflow()
        test_workflow.history = ['start', 'collect', 'fulfill', 'finish']
        workflow_manager.register_workflow(test_workflow)
        while True:
            data_recv = conn.recv(1024)
            if not data_recv:
                continue
            request = json.loads(data_recv)
            print 'request received:'
            print request
            reply = workflow_manager.process_request(request['workflow_id'], request['task'])
            # reply = workflow_manager.process_request(test_workflow.id, request['task'])
            conn.sendall(json.dumps(reply))
        conn.close()
    except socket.error as e:
        print 'bind_failed'
        sys.exit()
    finally:
        sock.close()


if __name__ == '__main__':
    start_server()
