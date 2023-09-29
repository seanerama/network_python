from netmiko import ConnectHandler
from getcreds import get_credentials

user, pwd = get_credentials()

command = 'show clock'
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
result = ssh.send_command(command)
ssh.disconnect()
print(result)



