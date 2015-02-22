import sys

from workflow import Workflow

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


def main(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`

    # Your imports here if you want to catch import errors

    # Get args from Workflow as normalized Unicode
    args = wf.args

    # Do stuff here ...
    from awsboto import search_instances, instance_to_string

    instances = search_instances(QUERY)

    if len(instances) > 0:
        for i in instances:
            # Add an item to Alfred feedback
            wf.add_item(instance_to_string(i), i.instance_type + ", " + i.key_name,
                        arg=i.ip_address,
                        valid=True,)
    else:
        wf.add_item('None found', 'Item subtitle')

    # Send output to Alfred
    wf.send_feedback()
