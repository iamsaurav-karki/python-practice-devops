import os

def get_env():
    return os.getenv('password')

def get_env_token():
    return os.getenv('apitoken')
    
print(get_env())
print(get_env_token())