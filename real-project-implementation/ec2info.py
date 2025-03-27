ec2_instances_info = [

  {
    "instance_id": "i-12345678",
    "instance_type": "t2.micro",
    "instance_state": "running",
    "public_ip": "2.34.2.3"

  },
  {
    "instance_id": "i-23456789",
    "instance_type": "t2.small",
    "instance_state": "stopped",
    "public_ip": ""
  },
  {
    "instance_id": "i-34567890",
    "instance_type": "t2.medium",
    "instance_state": "running",
    "public_ip": "3.45.23.298"
  },
  {
    "instance_id": "i-45678901",
    "instance_type": "t2.large",
    "instance_state": "stopped",
    "public_ip": "4.34.2.3"
  }
]

print(ec2_instances_info[0])
print(ec2_instances_info[0]["instance_type"])
