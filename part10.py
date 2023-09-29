import csv
import concurrent.futures
from netmiko import ConnectHandler
from getcreds import get_credentials

def get_commands():
    """Prompt the user to enter up to 25 'show' commands interactively."""
    commands = []
    print("Enter up to 25 'show' commands. Type 'done' when you are finished:")
    while len(commands) < 25:
        command = input("Enter a 'show' command or 'done': ").strip()
        if command.lower() == 'done':
            break
        elif command.startswith('show '):
            commands.append(command)
        else:
            print("Invalid command. Please enter a 'show' command or 'done'.")
    return commands

def get_switches(filename='switches100.txt'):
    """Read a list of IPs from a text file."""
    with open(filename, 'r', encoding='utf-8-sig') as switch_file:
        switches = [line.strip() for line in switch_file]
    return switches

def connect_and_run_commands(device, commands):
    """Establish an SSH connection to a device and execute a list of commands on it."""
    try:
        ssh = ConnectHandler(**device)
        print(f"Successfully connected to {device['host']}")
        ip_results = [device['host']]
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
    N = 10  # Number of threads, adjust as needed
    
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['IP'] + commands)
        
        # Create a ThreadPoolExecutor with N threads
        with concurrent.futures.ThreadPoolExecutor(max_workers=N) as executor:
            # Create a list of futures, each representing a task to be executed in a separate thread
            futures = []
            for ip in switches:
                device = {
                    'device_type': 'cisco_ios',
                    'host': ip,
                    'username': user,
                    'password': pwd,
                    'secret': pwd,
                    'port': 22,
                }
                futures.append(executor.submit(connect_and_run_commands, device, commands))
            
            # As the futures complete, write the results to the CSV file
            for future in concurrent.futures.as_completed(futures):
                writer.writerow(future.result())

if __name__ == "__main__":
    main()
