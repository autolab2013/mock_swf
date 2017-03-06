# -*- coding utf-8 -*-

class WorkflowManager(object):
    def __init__(self):
        self.workflow_records = {}

    def process_request(self, workflow_id, task):
        workflow = self.workflow_records.get(workflow_id, None)
        if not workflow:
            return 'workflow not found'
        else:
            return getattr(self, task)(workflow)

    def register_workflow(self, workflow):
        self.workflow_records.update({workflow.id: workflow})
        return True

    def get_history(self, workflow):
        return workflow.history

