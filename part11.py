import csv
import concurrent.futures
from netmiko import ConnectHandler
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from getcreds import get_credentials, get_email_params

def get_commands():
    """Prompt the user to enter up to 25 'show' commands interactively."""
    commands = []
    email = input("Input your email address: ")
    print("Enter up to 25 'show' commands. Type 'done' when you are finished:")
    while len(commands) < 25:
        command = input("Enter a 'show' command or 'done': ").strip()
        if command.lower() == 'done':
            break
        elif command.startswith('show '):
            commands.append(command)
        else:
            print("Invalid command. Please enter a 'show' command or 'done'.")
    return commands, email

def get_switches(filename='switches3.txt'):
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
    commands, email = get_commands()
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
    
    print(sendemail(email,'results.csv'))

def sendemail(email_addr, filename):
    # Create the email
    msg = MIMEMultipart()
    send_server, from_email = get_email_params()
    msg['From'] = from_email
    msg['To'] = email_addr
    msg['Subject'] = 'Requested show commands'

    # Attach the CSV file
    with open(filename, 'rb') as file:
        attach_file = MIMEBase('application', 'octet-stream')
        attach_file.set_payload(file.read())
        encoders.encode_base64(attach_file)
        attach_file.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file.name))
        msg.attach(attach_file)
    
    # Set up the SMTP server settings
    with smtplib.SMTP(send_server, 25) as smtp:
        smtp.starttls()
        smtp.send_message(msg)
    return "Email has been sent to " + email_addr

if __name__ == "__main__":
    main()
