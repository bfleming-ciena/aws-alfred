import sys

from workflow import Workflow
from awsboto import search_instances, save_config, instance_to_string

QUERY = ''


def run(query):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`
    # Your imports here if you want to catch import errors
    # or if the modules/packages are in a directory added via `Workflow(libraries=...)`
    # Get args from Workflow, already in normalised Unicode
    global QUERY
    QUERY = query.lower()
    wf = Workflow()
    sys.exit(wf.run(main))


def run_aws_save_config(query):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`
    # Your imports here if you want to catch import errors
    # or if the modules/packages are in a directory added via `Workflow(libraries=...)`
    # Get args from Workflow, already in normalised Unicode
    global QUERY
    QUERY = query.lower()
    wf = Workflow()
    sys.exit(wf.run(aws_save_config))


def aws_save_config(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`
    # Your imports here if you want to catch import errors
    # or if the modules/packages are in a directory added via `Workflow(libraries=...)`
    # Get args from Workflow, already in normalised Unicode
    # global QUERY
    # QUERY = query.lower()
    save_config(QUERY)
    # Send output to Alfred
    wf.add_item('Press enter to save.', arg='saved', valid=True)
    wf.send_feedback()

    # wf = Workflow()
    # sys.exit(wf.run(main))


def main(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`

    # Your imports here if you want to catch import errors

    # Get args from Workflow as normalized Unicode
    args = wf.args

    # Do stuff here ...

    instances = search_instances(QUERY)

    if len(instances) > 0:
        for i in instances:
            # Add an item to Alfred feedback
            wf.add_item(str(instance_to_string(i)), str(i.instance_type) + ", " + str(i.key_name),
                        arg=i.ip_address,
                        valid=True,)
    else:
        wf.add_item('None found', 'Item subtitle')

    # Send output to Alfred
    wf.send_feedback()
