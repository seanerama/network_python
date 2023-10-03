from ntc_templates.parse import parse_output
from netmiko import ConnectHandler
from getcreds import get_credentials

user, pwd = get_credentials()

command = 'show ip route'
ip = '<ROUTER IP>'

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
#print(result)

routing_parsed = parse_output(platform="cisco_ios", command="show ip route", data=result)

for route in routing_parsed:
    print("Network: " + route['network'] +'/' + route['mask'] + " ----NEXT HOP-----> " + route['nexthop_ip'])

