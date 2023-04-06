import boto3

# create aws client and resource
ec2_client = boto3.client('ec2', region_name="us-east-1")
ec2_resource = boto3.resource('ec2', region_name="us-east-1")

# create new vpc
new_vpc = ec2_resource.create_vpc(
    CidrBlock="10.0.0.0/16"
)

# create two new subnets
new_vpc.create_subnet(
    CidrBlock="10.0.1.0/24"
)
new_vpc.create_subnet(
    CidrBlock="10.0.2.0/24"
)

# create tags for the vpc created
new_vpc.create_tags(
    Tags=[
        {
            'Key': 'Name',
            'Value': 'my-vpc'
        },
    ]
)








