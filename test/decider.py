# -*- coding utf-8 -*-
import json
import socket

import ipdb; ipdb.set_trace()

from base_batch import BatchBase

class Decider(BatchBase):
    def job(self, *args, **kwargs):
        for arg in args:
            print arg
        print kwargs

    def get_workflow_execution_history(self, workflow_id):
        return self.quest_server({'task': 'get_history', 'workflow_id': workflow_id})

    def run(self):
        # test get history
        print self.get_workflow_execution_history('test')


if __name__ == '__main__':
    decider = Decider()
    decider.run()

