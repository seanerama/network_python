from netmiko import ConnectHandler
from getcreds import get_credentials

user, pwd = get_credentials()

#now a list of commands
commands = ['show clock', 'show run | i hostname ', 'show ver | i Last reload reason:']

#now we will read a list of IPs from a text file. 
with open('switche3.txt', 'r', encoding='utf-8-sig') as switch_file:
    switches = [line.strip() for line in switch_file]


#new for loop for each ip in ips
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

        results = ''

        #Using a for loop to cycle through commands. 

        for command in commands:
                results = results + ssh.send_command(command) + '\n \n'

        ssh.disconnect()

        print(results)



