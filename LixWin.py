import boto3

client = boto3.client('ec2', region_name='us-east-1')  # You can change region as needed

response = client.run_instances(
    ImageId='ami-00a929b66ed6e0de6',
    InstanceType='t2.micro',

    KeyName='USKEY3', # Changed USKEY1 TO USKEY3 by Linux Dev.He didn't Pull. So, not updated 

   # Changed USKEY1 TO USKEY2 by the windows Dev

    MinCount=1,
    MaxCount=1
)

print("EC2 Instance launched!")
print(response['Instances'][0]['InstanceId'])
