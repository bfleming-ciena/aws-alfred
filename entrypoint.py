import sys

from workflow import Workflow
from awsboto import start_instance, stop_instance, search_instances, save_config, instance_to_string


def ec2_gen_search(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`

    # Your imports here if you want to catch import errors

    # Get args from Workflow as normalized Unicode
    if len(wf.args) > 0:
        query = wf.args[0]
        argname = wf.args[2]
        wf.logger.debug(argname)

    instances = search_instances(query)

    if len(instances) > 0:
        for i in instances:
            # Add an item to Alfred feedback

            val = getattr(i, argname)
            wf.add_item(str(instance_to_string(i)), str(i.instance_type) + ", " + str(i.key_name),
                        arg=val,
                        valid=True,)
    else:
        wf.add_item('None found', 'Item subtitle', arg="NO IP", valid=True)

    # Send output to Alfred
    wf.send_feedback()


def ec2_start_search(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`

    # Your imports here if you want to catch import errors

    # Get args from Workflow as normalized Unicode
    if len(wf.args) > 0:
        query = wf.args[0]
        # wf.logger.debug("Alfred Args Sent: " + str(wf.args) + "length=" + str(len(wf.args)))

    # Do stuff here ...

    instances = search_instances(query)

    if len(instances) > 0:
        for i in instances:
            # Add an item to Alfred feedback

            wf.add_item(str(instance_to_string(i)), str(i.instance_type) + ", " + str(i.key_name),
                        arg=i.id,
                        valid=True,)
    else:
        wf.add_item('None found', 'Item subtitle', arg="NO IP", valid=True)

    # Send output to Alfred
    wf.send_feedback()


def ec2_stop_instance(id):

    wf.logger.debug(wf.args)
    if len(wf.args) > 0:
        id = wf.args[0]
        wf.logger.debug(stop_instance(id))
        wf.add_item('None found', 'Item subtitle',
                    arg="Instance started", valid=True)

    wf.send_feedback()


def ec2_start_instance(id):

    wf.logger.debug(wf.args)
    if len(wf.args) > 0:
        id = wf.args[0]
        wf.logger.debug(start_instance(id))
        wf.add_item('None found', 'Item subtitle',
                    arg="Instance started", valid=True)

    wf.send_feedback()


def aws_save_config(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`
    # Your imports here if you want to catch import errors
    # or if the modules/packages are in a directory added via `Workflow(libraries=...)`
    # Get args from Workflow, already in normalised Unicode
    # global QUERY
    # QUERY = query.lower()
    if len(wf.args) > 0:
        query = wf.args[0]
        # wf.logger.debug("Alfred Args Sent: " + str(wf.args) + "lenght=" + str(len(wf.args)))

    save_config(query)
    # Send output to Alfred
    wf.add_item('Press enter to save.', arg='saved', valid=True)
    wf.send_feedback()

    # wf = Workflow()
    # sys.exit(wf.run(main))


def ec2_search(wf):

    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`

    # Your imports here if you want to catch import errors

    # Get args from Workflow as normalized Unicode
    if len(wf.args) > 0:
        query = wf.args[0]
        # wf.logger.debug("Alfred Args Sent: " + str(wf.args) + "length=" + str(len(wf.args)))

    # Do stuff here ...

    instances = search_instances(query)

    if len(instances) > 0:
        for i in instances:
            # Add an item to Alfred feedback

            if i.ip_address is not None:
                ip = i.ip_address
            else:
                ip = "No IP Address"

            wf.add_item(str(instance_to_string(i)), str(i.instance_type) + ", " + str(i.key_name),
                        arg=ip,
                        valid=True,)
    else:
        wf.add_item('None found', 'Item subtitle', arg="NO IP", valid=True)

    # Send output to Alfred
    wf.send_feedback()

if __name__ == "__main__":
    wf = Workflow()
    f = wf.args[1]  # args expected: <query> <subcmd>
    thismodule = sys.modules[__name__]
    fref = getattr(thismodule, f)
    sys.exit(wf.run(fref))
