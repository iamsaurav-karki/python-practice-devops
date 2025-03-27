"""
Backup files to S3
"""
import boto3
import os
import shutil
import tempfile

s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3, bucket_name, region):
    try:
        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print("Bucket created successfully")
    except s3.meta.client.exceptions.BucketAlreadyOwnedByYou:
        print(f"Bucket {bucket_name} already exists and is owned by you")

def upload_backup(s3, source_path, bucket_name, key_name):
    try:
        if os.path.isfile(source_path):
            # Upload single file
            with open(source_path, 'rb') as data:
                s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
        elif os.path.isdir(source_path):
            # Create a temporary tar.gz file
            with tempfile.NamedTemporaryFile(suffix='.tar.gz', delete=False) as tmp:
                temp_path = tmp.name
            try:
                # Create archive
                shutil.make_archive(temp_path.replace('.tar.gz', ''), 'gztar', source_path)
                # Upload archive
                with open(temp_path, 'rb') as data:
                    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
            finally:
                # Clean up temporary file
                if os.path.exists(temp_path):
                    os.remove(temp_path)
        else:
            raise ValueError(f"Source path {source_path} is neither a file nor a directory")
        print("Backup uploaded successfully")
    except Exception as e:
        print(f"Error uploading backup: {e}")

# Configuration
bucket_name = "my-boto3-bucket221"
region = "us-west-2"
source_path = "D:/python-for-devops/real-project-implementation/backups"

# Execute
create_bucket(s3, bucket_name, region)
show_buckets(s3)
upload_backup(s3, source_path, bucket_name, "my-backup.tar.gz")