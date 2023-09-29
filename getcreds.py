def get_credentials(filename='credentials.txt'):
    """Read credentials from a text file."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    credentials = {}
    for line in lines:
        key, value = line.strip().split('=')
        credentials[key] = value
    
    return credentials['usr'], credentials['pwd']

def get_email_params(filename='credentials.txt'):
    """Read credentials from a text file."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    credentials = {}
    for line in lines:
        key, value = line.strip().split('=')
        credentials[key] = value
    
    return credentials['send_server'], credentials['send_email']
