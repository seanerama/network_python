from netmiko import ConnectHandler
from getcreds import get_credentials

user, pwd = get_credentials()

#now a list of commands
commands = ['show clock', 'show run | i hostname ', 'show ver | i Last reload reason:']
ip = '<ENTER THE IP OF A DEVICE HERE>'

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



