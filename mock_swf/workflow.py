# -*- coding: utf-8 -*-

import uuid

class Workflow(object):
    def __init__(self):
        # generate a random uuid: https://docs.python.org/2/library/uuid.html
        self.id = uuid.uuid4()
        self.history = []
        self.curr_state = None
        self.next_state = None



