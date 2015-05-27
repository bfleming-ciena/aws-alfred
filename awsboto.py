import boto.ec2
import yaml


def save_config(query):
    config = dict(([x.split('=') for x in query.split(',')]))
    stream = file('./aws.conf', 'w')
    # config['region'] = query
    yaml.dump(config, stream)


def load_config():
    stream = file('./aws.conf', 'r')
    return yaml.load(stream)


def get_instances():

    config = load_config()
    if 'region' in config:
        region = config['region']
    else:
        region = 'us-west-2'

    boto_ec2 = boto.ec2.connect_to_region(region)
    rsv = boto_ec2.get_all_instances()
    idata = {}
    for r in rsv:
        i = r.instances[0]
        tag_value = i.tags.get('Name', '')
        idata[i.id + ", " + tag_value + ", " + str(i.ip_address) + ", " + i.state] = i
    return idata


def start_instance(id):
    config = load_config()
    if 'region' in config:
        region = config['region']
    else:
        region = 'us-west-2'

    boto_ec2 = boto.ec2.connect_to_region(region)
    instance = boto_ec2.get_all_instances(instance_ids=[id])
    return instance[0].instances[0].start()


def stop_instance(id):
    config = load_config()
    if 'region' in config:
        region = config['region']
    else:
        region = 'us-west-2'

    boto_ec2 = boto.ec2.connect_to_region(region)
    instance = boto_ec2.get_all_instances(instance_ids=[id])
    return instance[0].instances[0].stop()


def instance_to_string(i):
    #if 'Name' in i.tags.keys():
    tag_value = i.tags.get('Name', '')
    return i.id + ", " + tag_value + ", " + str(i.ip_address) + ", " + i.state


def search_instances(query):
    # CACHE['expires'] = 30 # Seconds to expire cache
    idata = get_instances()
    search_results = []
    for k in idata.keys():
        stringify_instance = ("".join(str(idata[k].__dict__.values()))).lower()
        queries = query.split(" ")
        match = 0
        for q in queries:
            if q in stringify_instance:
                match = match + 1

        if match == len(queries):  # all user queries matched, we got a winner.
            search_results.append(idata[k])

    return search_results


if __name__ == "__main__":
    import sys
    for i in search_instances(sys.argv[1]):
        print instance_to_string(i)
