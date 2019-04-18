import netmiko
import datetime
import getpass

username = input("Username: ")
password = getpass.getpass("Password: ")
ios = "cisco_ios"
print("\n" + "Please wait just a moment! The script is starting up and will print out its progress soon.")

log_file = open("syslog_logfile.txt", "a")
with open("device_list.txt") as f:
    device_line = f.read().splitlines()
while("" in device_line):
    device_line.remove("")
device_list = device_line

start_time = datetime.datetime.now()


def connect_success():
    print("Successfully connected to: {}".format(host_name))
    print("Sending commands now... ")


def save():
    print("Saving configuration now... ")
    connect.send_command("wr mem")
    print("Configuration saved successfully!")
    print("=" * 60)


def nxos_save():
    print("Saving configuration now... ")
    connect.send_command("copy run start")
    print("Configuration saved successfully!")
    print("=" * 60)


def router_syslog():
    host = connect.send_command("sh run | in hostname")
    host_name = host.split()[1]
    if "dc1" in host.lower():
        dc1_asr_syslog = "path/to/dc1/router/config"
        connect_success()
        connect.send_config_from_file(dc1_asr_syslog)
        print("Syslog configured successfully!")
        save()
    elif "dc2" in host.lower():
        dc2_asr_syslog = "path/to/dc2/router/config"
        connect_success()
        connect.send_config_from_file(dc2_asr_syslog)
        print("Syslog configured successfully!")
        save()
    elif "dc3" in host.lower():
        dc3_asr_syslog = "path/to/dc3/router/config"
        connect_success()
        connect.send_config_from_file(dc3_asr_syslog)
        print("Syslog configured successfully!")
        save()
    elif "dc4" in host.lower():
        dc4_asr_syslog = "path/to/dc4/router/config"
        connect_success()
        connect.send_config_from_file(dc4_asr_syslog)
        print("Syslog configured successfully!")
        save()
    elif "dc5" in host.lower():
        dc5_asr_syslog = "path/to/dc5/router/config"
        connect_success()
        connect.send_config_from_file(dc5_asr_syslog)
        print("Syslog configured successfully!")
        save()
    else:
        print("Hostname could not be associated with a known DC. Moving on to next device.")


def ios_syslog():
    host = connect.send_command("sh run | in hostname")
    host_name = host.split()[1]
    if "dc1" in host.lower():
        dc1_ios_syslog = "path/to/dc1/ios/config"
        connect_success()
        connect.send_config_from_file(dc1_ios_syslog)
        print("Syslog configured successfully!")
        save()
    elif "dc2" in host.lower():
        dc2_ios_syslog = "path/to/dc2/router/config"
        connect_success()
        connect.send_config_from_file(dc2_ios_syslog)
        print("Syslog configured successfully!")
        save()
    elif "dc3" in host.lower():
        dc3_ios_syslog = "path/to/dc3/router/config"
        connect_success()
        connect.send_config_from_file(dc3_ios_syslog)
        print("Syslog configured successfully!")
        save()
    elif "dc4" in host.lower():
        dc4_ios_syslog = "path/to/dc4/router/config"
        connect_success()
        connect.send_config_from_file(dc4_ios_syslog)
        print("Syslog configured successfully!")
        save()
    elif "dc5" in host.lower():
        dc5_ios_syslog = "path/to/dc5/router/config"
        connect_success()
        connect.send_config_from_file(dc5_ios_syslog)
        print("Syslog configured successfully!")
        save()
    else:
        print("Hostname could not be associated with a known DC. Moving on to next device.")


def nxos_syslog():
    host = connect.send_command("sh hostname")
    host_name = host.split()[1]
    if "dc1" in host.lower():
        dc1_nxos_syslog = "path/to/dc1/nxos/config"
        connect_success()
        connect.send_config_from_file(dc1_nxos_syslog)
        print("Syslog configured successfully!")
        save()
    elif "dc2" in host.lower():
        dc2_nxos_syslog = "path/to/dc2/nxos/config"
        connect_success()
        connect.send_config_from_file(dc2_nxos_syslog)
        print("Syslog configured successfully!")
        save()
    elif "dc3" in host.lower():
        dc3_nxos_syslog = "path/to/dc3/nxos/config"
        connect_success()
        connect.send_config_from_file(dc3_nxos_syslog)
        print("Syslog configured successfully!")
        save()
    elif "dc4" in host.lower():
        dc4_nxos_syslog = "path/to/dc4/nxos/config"
        connect_success()
        connect.send_config_from_file(dc4_nxos_syslog)
        print("Syslog configured successfully!")
        save()
    elif "dc5" in host.lower():
        dc5_nxos_syslog = "path/to/dc5/nxos/config"
        connect_success()
        connect.send_config_from_file(dc5_nxos_syslog)
        print("Syslog configured successfully!")
        save()
    else:
        print("Hostname could not be associated with a known DC. Moving on to next device.")


for device in device_list:
    print("Now connecting to: {}".format(device))
    connect = netmiko.ConnectHandler(username=username, password=password, device_type=ios, ip=device)

    print("Successfully connected to: {}".format(device))
    platform = connect.send_command("sh version")
    host = connect.send_command("sh run | in hostname")
    host_name = host.split()[1]

    if "CONDITION MET" in hostname.lower() or "CONDITION MET" in platform:
        print("Non-configurable device detected. Moving on to next device.")
        continue
    if "asr" in platform or "isr" in platform:
        router_syslog()
    elif "2960" in platform or "3560" in platform or "3850" in platform or "3650" in platform:
        ios_syslog()
    elif "nx-os" in platform.lower():
        nxos_syslog()
