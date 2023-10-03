import requests

def arin_whois(ip):
    """
    Queries the ARIN Whois database to retrieve organization details for a given IP address.
    
    Parameters:
    - ip (str): The IP address to look up.
    
    Returns:
    - str: A formatted string containing the IP address, organization handle, and organization name.
    """
    
    url = f"https://whois.arin.net/rest/ip/{ip}.json"
    response = requests.get(url)
    data = response.json()

    # Extracting organization details
    org_handle = data['net']['orgRef']['@handle']
    org_name = data['net']['orgRef']['$']

    # Formatting the response into a single variable
    res = (f"IP Address: {ip}\n"
           f"Organization Handle: {org_handle}\n"
           f"Organization Name: {org_name}")

    return res

print(arin_whois('IPADDRESS'))
