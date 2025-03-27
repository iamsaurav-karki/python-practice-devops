
def update_server_config_file(file_path, key, value):
    # Read the server config file
    with open(file_path, 'r') as file:
      lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                file.write(f'{key}: {value}\n')
            else:
                file.write(line)

update_server_config_file('server.conf', 'MAX_CONNECTIONS', '21')
      