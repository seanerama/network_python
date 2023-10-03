from netmiko import ConnectHandler
from getcreds import get_credentials
from time import sleep
import re

user, pwd = get_credentials()


def get_running_config(ip, os):
    """Establish an SSH connection to a device and retrieve the running config."""
    device = {
        'device_type': os,
        'host': ip,
        'username': user,
        'password': pwd,
        'secret': pwd,
        'port': 22,
        'timeout': 60
    }

    try:
        with ConnectHandler(**device) as ssh:
            print(f"Successfully connected to {ip}")
            return ssh.send_command('show run')
    except Exception as e:
        print(f"Failed to connect to {ip} or execute commands: {e}")


def detect_os(ip):
    """Detect the operating system of the device."""
    device = {
        'device_type': 'cisco_xe',
        'ip': ip,
        'username': user,
        'password': pwd,
        'timeout': 60,
    }

    try:
        with ConnectHandler(**device) as ssh:
            print(f"Successfully connected to {ip}")
            sleep(3)
            output = ssh.send_command('show ver')

            if 'NX-OS' in output:
                return 'cisco_nxos'
            elif 'IOS XR' in output:
                return 'cisco_xr'
            elif 'Cisco IOS' in output:
                return 'cisco_ios'
            else:
                return 'unknown'
    except Exception as e:
        print(f"Failed to connect to {ip} or execute commands: {e}")


def get_device_vars(ip):
    """Retrieve device attributes."""
    os_type = detect_os(ip)
    print(f"{ip} detected os: {os_type}")
    config = get_running_config(ip, os_type)

    hostname_match = re.search(r'hostname (\S+)', config)
    hostname = hostname_match.group(1) if hostname_match else None

    return {
        'ip': ip,
        'hostname': hostname,
        'os': os_type
    }
