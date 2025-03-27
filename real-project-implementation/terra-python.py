import subprocess
def terraform_init(command):
  process = subprocess.run(command,shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  return process.stdout.decode('utf-8')

directory = "D:/project/terraform" # path to your terraform files directory
command = f"terraform -chdir={directory} init"
terraform_init(command) # Run terraform init command

def terraform_plan(command):
  process = subprocess.run(command,shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  return process.stdout.decode('utf-8')

command = f"terraform -chdir={directory} plan"
terraform_plan(command) # Run terraform plan command

def terraform_apply(command):
  process = subprocess.run(command,shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
  return process.stdout.decode('utf-8')

command = f"terraform -chdir={directory} apply -auto-approve"
terraform_apply(command) # Run terraform apply command
