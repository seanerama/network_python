from ntc_templates.parse import parse_output
from netmiko import ConnectHandler
from getcreds import get_credentials

user, pwd = get_credentials()

command = 'show cdp nei'
ip = '<IP>'

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

cdp_parsed = parse_output(platform="cisco_ios", command="show cdp neighbors", data=result)

for device in cdp_parsed:
    print(device['neighbor'] + '(' + device['platform'] + ')' + ' is connected to interface ' + device['local_interface'] + "\n")
    

