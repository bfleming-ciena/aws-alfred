# aws-alfred
AWS Workflow for Alfred2

Example Usage:

    aws config region=us-west-2

    ec2 {any string}   (copies the IP to the clipboard)

    ec2 start {any string}

    ec2 stop {any string}

Searches EC2 instances. Type anything. All instance properties will be searched.

## Requirements
Uses the python boto module.  You only need python, or at least should.  All required python modules should be present in the workflow. No need to install them.

However you need to have the following file.

~/.boto

[Credentials]
aws_access_key_id=[Yours]
aws_secret_access_key=[Yours]


## The Workflow Itself
1) Create a new command by creating a new keyword with arg, and change it to bash script. Here is an example.

    python entrypoint.py "{query}" "ec2_gen_search" "ip_address"

arg1: The query, given by alfred.

arg2: Function to call

arg3: The value of the instance field you want passed on (see boto docs), but some examples are "ip_address" and "id".  I use this for example, to send the ip_address to a copy clipboard response so I can use the IP for an SSH.
