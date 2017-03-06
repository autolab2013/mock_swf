mock_swf is my implementation of SWF. It aims to reproduce the functionality of AWS SimpleWorkflow.

SimpleWorkflow is a queue with additional functionalities. Message enqueued is more like a state to a state machine, as this queue serves for coordination a workflow that user can specify. 

Core concepts: a workflow is a flow of state transitions, with certain activity needs to be done for each state.
- workflow: can seen as an instance of a state machine.

The message can be divided into 3 types:
- workflow message:  This contains workflow_start and workflow_end, marking the start and end of a workflow.
- decision message: This represents the state. Based on this SWF can know what next state is and what activity it should do for current state. Note decision only represent states and does no actual work corresponding to this state.
- activity message: This represents the actual work needs to be carried out, like a collection activity would mean call to processor and collect the right money.

Messages are considered tasks. When workflow_start message receivd, SWF will schedule decion task for decider to pickup. After decider pick up decison task and response with decision message, SWF will schedule activity task based on decision message. When the final state of workflow is reached, decider will respond with workflow_finish to notify SWF the workflow has finished.

Aside from that, SWF provides timeout and retry mechanism.  
- workflow level timeout: how long the workflow takes from start to finish
- decision level timeout: how long a decision task can take from start to finish
- activity level timeout: how long a activity can take from start to finish, how long from task is scheduled to get picked up, how long from scheduled to finish, how long acitivty can run before providing heartbeat
