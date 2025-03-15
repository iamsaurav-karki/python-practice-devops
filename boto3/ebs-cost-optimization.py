import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

def get_active_volume_ids():
    """Get volume IDs from running instances"""
    volumes = set()
    paginator = ec2.get_paginator('describe_instances')
    
    for page in paginator.paginate(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]):
        for reservation in page['Reservations']:
            for instance in reservation['Instances']:
                for block in instance.get('BlockDeviceMappings', []):
                    if 'Ebs' in block:
                        volumes.add(block['Ebs']['VolumeId'])
    return volumes

def get_associated_snapshots(volume_ids):
    """Get snapshots created from active volumes"""
    associated_snaps = set()
    for volume_id in volume_ids:
        response = ec2.describe_snapshots(
            Filters=[{'Name': 'volume-id', 'Values': [volume_id]}]
        )
        associated_snaps.update(snap['SnapshotId'] for snap in response['Snapshots'])
    return associated_snaps

def find_orphaned_snapshots(associated_snaps):
    """Find all snapshots not linked to current volumes"""
    all_snaps = set()
    paginator = ec2.get_paginator('describe_snapshots')
    
    for page in paginator.paginate(OwnerIds=['self']):
        for snap in page['Snapshots']:
            all_snaps.add(snap['SnapshotId'])
    
    return all_snaps - associated_snaps

def clean_orphaned_snapshots(dry_run=False):
    """Main cleanup function with dry-run protection"""
    try:
        active_volumes = get_active_volume_ids()
        good_snapshots = get_associated_snapshots(active_volumes)
        orphaned = find_orphaned_snapshots(good_snapshots)

        print(f"Found {len(orphaned)} orphaned snapshots")
        
        if not dry_run:
            for snap_id in orphaned:
                ec2.delete_snapshot(SnapshotId=snap_id)
                print(f"Deleted {snap_id}")
        
        return {
            'statusCode': 200,
            'body': f"Dry run: Would delete {len(orphaned)} snapshots" if dry_run 
                   else f"Deleted {len(orphaned)} snapshots"
        }
    
    except ClientError as e:
        print(f"Error: {e}")
        return {'statusCode': 500, 'body': "Execution failed"}

# Example usage (Set dry_run=False to actually delete)
def lambda_handler(event, context):
    return clean_orphaned_snapshots(dry_run=False)