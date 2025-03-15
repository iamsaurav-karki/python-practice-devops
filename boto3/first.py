import boto3
# Create an S3 client
s3 = boto3.client('s3')
response = s3.create_bucket(
  Bucket='my-boto3-bucket221'
  )

# list all the buckets
response = s3.list_buckets()
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


complete_response = s3.get_bucket_acl(
    Bucket='my-boto3-bucket221'
)
print(complete_response)

# delete the bucket
response = s3.delete_bucket(
    Bucket='my-boto3-bucket221'
)