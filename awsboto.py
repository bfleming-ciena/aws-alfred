import boto.ec2


def get_instances():
    boto_ec2 = boto.ec2.connect_to_region("us-west-2")
    rsv = boto_ec2.get_all_instances()
    idata = {}
    for r in rsv:
        i = r.instances[0]
        if 'Name' in i.tags.keys():
            # import ipdb
            # ipdb.set_trace()
            tag_value = i.tags['Name']
            idata[i.id + ", " + tag_value + ", " + str(i.ip_address) + ", " + i.state] = i
    return idata


def instance_to_string(i):
    if 'Name' in i.tags.keys():
        tag_value = i.tags['Name']
        return i.id + ", " + tag_value + ", " + str(i.ip_address) + ", " + i.state


def search_instances(query):
    # CACHE['expires'] = 30 # Seconds to expire cache
    idata = get_instances()

    search_results = []
    for k in idata.keys():
        stringify_instance = ("".join(str(idata[k].__dict__.values()))).lower()
        if query in stringify_instance:
            search_results.append(idata[k])

    return search_results


if __name__ == "__main__":
    import sys
    for i in search_instances(sys.argv[1]):
        print instance_to_string(i)
