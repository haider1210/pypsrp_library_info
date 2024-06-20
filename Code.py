# How to connenct remote powershell by using credentials and run the powershell commands from another devices by using python.


# Get all vms  using Commands 

from pypsrp.client import Client
server = [ "10.1--.1.5.1--","ex2"]
username = "useraname" #Note that actual username consists of only one backslash, but in python two are given for escaping the single backslash.
password = "password"

print("Output:")
for srvr in server:
    with Client(srvr, username=username, password=password, ssl=False) as client:
        command = """powershell.exe -Command "Get-VM" """
        stdout, stderr, rc = client.execute_cmd(command)
        print(f"server :{srvr}\n")
        print(stdout)
        print(stderr)


# Get vm details using scripts

from pypsrp.client import Client

server = "10.130.----"
username = "usernaem" #Note that actual username consists of only one backslash, but in python two are given for escaping the single backslash.
password = "password"

with Client(server, username=username, password=password, ssl=False) as client:
    stdout, stderr, rc = client.execute_cmd("""powershell.exe C:\-------\----\scripts\get-vm-details.ps1 -vm_name haider -uri "https://-----------.co.in" -secusername "-----------" -secpasswd "-------" """)
    print("OUTPUT:")
    print(stdout)
    print("\nERRORS:")
    print(stderr)
