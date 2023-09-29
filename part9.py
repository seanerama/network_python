import csv
from netmiko import ConnectHandler
from getcreds import get_credentials


def get_commands():
    """
    This function prompts the user to enter up to 25 'show' commands interactively.
    It returns a list of strings, each string being a command entered by the user.
    """
    commands = []
    print("Enter up to 25 'show' commands. Type 'done' when you are finished:")
    while len(commands) < 25:
        command = input("Enter a 'show' command or 'done': ").strip()
        if command.lower() == 'done':
            break
        elif command.startswith('show '):  # Ensure the command is a 'show' command
            commands.append(command)
        else:
            print("Invalid command. Please enter a 'show' command or 'done'.")
    return commands

def get_switches(filename='switches3.txt'):
    """
    This function reads a list of IPs from a text file.
    It returns a list of strings, each string being an IP address from the file.
    """
    with open(filename, 'r', encoding='utf-8-sig') as switch_file:
        switches = [line.strip() for line in switch_file]
    return switches

def connect_and_run_commands(device, commands):
    """
    This function establishes an SSH connection to a device and executes a list of commands on it.
    It returns a list of strings, each string being the result of a command executed on the device.
    """
    try:
        ssh = ConnectHandler(**device)
        print(f"Successfully connected to {device['host']}")
        
        # Initialize a list to hold the results for this IP.
        ip_results = [device['host']]
        
        # Iterate over commands and execute them.
        for command in commands:
            result = ssh.send_command(command)
            ip_results.append(result)
        
        return ip_results
    
    except Exception as e:
        print(f"Failed to connect to {device['host']} or execute commands: {e}")
        return [device['host']] + ['Error'] * len(commands)
    
    finally:
        if 'ssh' in locals() and ssh.is_alive():
            ssh.disconnect()

def main():


    user, pwd = get_credentials()
    commands = get_commands()
    switches = get_switches()
    
    # Open the CSV file for writing.
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header row to the CSV file.
        writer.writerow(['IP'] + commands)
        
        # Iterate over each IP and execute commands.
        for ip in switches:
            device = {
                'device_type': 'cisco_ios',
                'host': ip,
                'username': user,
                'password': pwd,
                'secret': pwd,
                'port': 22,
            }
            
            ip_results = connect_and_run_commands(device, commands)
            
            # Write the results for this IP to the CSV file.
            writer.writerow(ip_results)

if __name__ == "__main__":
    main()
