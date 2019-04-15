from netmiko import Netmiko
import datetime
import getpass

device = input("What is the IP address you need to configure?: ")
username = input("Username: ")
password = getpass.getpass("Password: ")
print("\n" + "Please wait just a moment! The script is starting up and will print out its progress soon.")


start_time = datetime.datetime.now()

cisco1 = {
    "host": device,
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

connect = Netmiko(**cisco1)
connect.send_command("terminal length 0")
show_version = connect.send_command("show version")
version_line = show_version.splitlines()[0]


if "NX-OS" in version_line:
    # Initialize NX-OS NetFlow Configuration
    nxos_netflow = "/path/to/file/for/nxos"
    connect.send_command("send log 5 Starting NetFlow config now")
    nxos_netflow = connect.send_config_from_file(nxos_netflow)

    config = []
    interface_list = connect.send_command("sh int status | in trunk")
    lines = interface_list.splitlines()

    for line in lines:
        if "Po" in line:
            continue
            # Skips over port-channel interfaces since they don't support Flexible NetFlow
        interface = line.split()[0]
        config.append("interface " + interface)
        config.append(" ip flow monitor MONITOR_NAME_HERE input")
        config.append("!")
    "\n".join(config)
    print("Configuring trunk interfaces... ")
    connect.send_send_config_set(config)
    print("Saving configuration now... ")
    connect.send_comand("copy run start")
    print("Finished!")

elif "IOS-XE" in version_line:
    # Initializes IOS-XE NetFlow Configuration
    iosxe_netflow = "/path/to/file/for/ios_xe"
    connect.send_command("send log 5 Starting NetFlow config now")
    print("Starting configuration now... ")
    iosxe_netflow = connect.send_config_from_file(iosxe_netflow)

    config = []
    interface_list = connect.send_command("sh int status | in trunk")
    lines = interface_list.splitlines()

    for line in lines:
        if "Po" in line:
            continue
            # Skips over port-channel interfaces since they don't support Flexible NetFlow
        interface = line.split()[0]
        config.append("interface " + interface)
        config.append(" ip flow monitor MONITOR_NAME_HERE input")
        config.append("!")
    "\n".join(config)
    print("Configuring trunk interfaces...")
    connect.send_config_set(config)
    print("Saving configuration now... ")
    connect.send_command("wr mem")
    print("Finished!")

elif "IOS" in version_line:
    # Initializes IOS configuration
    ios_netflow = "/path/to/file/for/ios"
    connect.send_command("log 5 Starting NetFlow configuration now")
    ios = connect.send_config_from_file("ios_netflow")

    config = []
    interface_list = connect.send_command("show int status | in trunk")
    lines = interface_list.split()

    for line in lines:
        if "Po" in line:
            continue
        interface = line.split()[0]
        config.append("interface " + interface)
        config.append(" ip flow monitor MONITOR_NAME_HERE sampler SAMPLER_NAME_HERE input")
        config.append("!")
    "\n".join(config)
    connect.send_config_set(config)
    print("Configuring trunk interfaces now... ")
    print("Saving configuration now... ")
    connect.send_command("wr mem")
    print("Finished")