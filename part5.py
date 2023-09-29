from netmiko import ConnectHandler
from getcreds import get_credentials

user, pwd = get_credentials()

#list of commands
commands = ['show clock', 'show run | i hostname ', 'show ver | i Last reload reason:']

#read a list of IPs from a text file. 
with open('switches3.txt', 'r', encoding='utf-8-sig') as switch_file:
    switches = [line.strip() for line in switch_file]

results = ''
#for loop for each ip in ips
for ip in switches:
        cisco_router = {
                'device_type': 'cisco_ios',
                'host': ip,
                'username': user,
                'password': pwd,
                'secret': pwd,
                'port': 22,
        }

        ssh = ConnectHandler(**cisco_router)

        #Using a for loop to cycle through commands. 
        results = results + "\n \nResults for: " + ip + "\n"
        for command in commands:
                results = results + "   Command: " + command + ": \n     " + ssh.send_command(command) + '\n \n'

        ssh.disconnect()

# Write the results to a file.
with open('results.txt', 'a') as result_file:
        result_file.write(results)
        



