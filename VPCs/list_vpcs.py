import boto3

# create aws client and resource
ec2_client = boto3.client('ec2', region_name="us-east-1")
ec2_resource = boto3.resource('ec2', region_name="us-east-1")

# list vpcs in the configured region
available_vpcs = ec2_client.describe_vpcs() 
vpcs = (available_vpcs["Vpcs"])

for vpc in vpcs:
    print(f"VPC ID: {vpc['VpcId']}")
    if 'Tags' in vpc:
        for tag in vpc['Tags']:
            if tag['Key'] == 'Name':
                print(f"VPC Name: {tag['Value']}")
    else:
        print("VPC Name: This VPC has no tag name.")
    cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]
    for assoc_set in cidr_block_assoc_sets:
        print(assoc_set["CidrBlockState"])
