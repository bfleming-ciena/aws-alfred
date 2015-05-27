# aws-alfred
AWS Workflow for Alfred2

## Requirements
Uses the python boto module.  You only need python, or at least should.  All required python modules should be present in the workflow. No need to install them.

However you must setup the creds file:

~/.boto

    [Credentials]
    aws_access_key_id=[Yours]
    aws_secret_access_key=[Yours]

Example Usage:

Set the configuration.

    ec2 config region=us-west-2,ip_type=[private|public]

ec2 find -- Searches EC2 instances. Type anything, and multiple keywords. All instance properties will be searched.

    ec2 find {any string} {any string}  (copies the IP to the clipboard)
    example:
    ec2 find killroy running

The IP address will be copied to the clipboard on enter.

ec2 stop and start work the same as ec2 find, but will send stop or start commands.

    ec2 start {any string}
    ec2 stop {any string}

