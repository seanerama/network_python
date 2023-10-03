from ntc_templates.parse import parse_output
from netmiko import ConnectHandler
from getcreds import get_credentials

user, pwd = get_credentials()

command = 'show vlan'
ip = '<IP OF SWITCH>'

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

vlan_parsed = parse_output(platform="cisco_ios", command="show vlan", data=result)

for vlan in vlan_parsed:
    print(vlan)