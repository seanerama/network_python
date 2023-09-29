import csv
from netmiko import ConnectHandler
from getcreds import get_credentials

user, pwd = get_credentials()

# List of commands
commands = ['show clock', 'show run | i hostname ', 'show ver | i Last reload reason:']

# Read a list of IPs from a text file.
with open('switches-bad.txt', 'r', encoding='utf-8-sig') as switch_file:
    switches = [line.strip() for line in switch_file]

# Open the CSV file for writing.
with open('results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header row to the CSV file.
    writer.writerow(['IP'] + commands)
    
    # Iterate over each IP and execute commands.
    for ip in switches:
        cisco_router = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': user,
            'password': pwd,
            'secret': pwd,
            'port': 22,
        }
        
        try:
            ssh = ConnectHandler(**cisco_router)
            print(f"Successfully connected to {ip}")
            
            # Initialize a list to hold the results for this IP.
            ip_results = [ip]
            
            # Iterate over commands and execute them.
            for command in commands:
                result = ssh.send_command(command)
                ip_results.append(result)
                
            # Write the results for this IP to the CSV file.
            writer.writerow(ip_results)
            
        except Exception as e:
            print(f"Failed to connect to {ip} or execute commands: {e}")
        finally:
            if 'ssh' in locals() and ssh.is_alive():
                ssh.disconnect()
