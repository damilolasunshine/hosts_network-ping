import subprocess


def ping_hosts(hosts):
    reachable_hosts = []
    unreachable_hosts = []

    for host in hosts:
        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        if result.returncode == 0:
            reachable_hosts.append(host)
        else:
            unreachable_hosts.append(host)

    return reachable_hosts, unreachable_hosts


if __name__ == "__main__":
    hosts_to_ping = ["192.168.1.1", "8.8.8.8", "10.0.0.1"]
    reachable, unreachable = ping_hosts(hosts_to_ping)

    print("Reachable hosts:", reachable)
    print("Unreachable hosts:", unreachable)


import subprocess


def ping_hosts(hosts):
    reachable_hosts = []
    unreachable_hosts = []

    for host in hosts:
        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        if result.returncode == 0:
            reachable_hosts.append(host)
        else:
            unreachable_hosts.append(host)

    return reachable_hosts, unreachable_hosts


if __name__ == "__main__":
    hosts_to_ping = []

    # Continuous input loop
    while True:
        host = input("Enter a host to ping (or 'q' to quit): ")
        if host.lower() == 'q':
            break
        hosts_to_ping.append(host)

    reachable, unreachable = ping_hosts(hosts_to_ping)

    print("Reachable hosts:", reachable)
    print("Unreachable hosts:", unreachable)


import subprocess
import re


def ping_hosts(hosts):
    reachable_hosts = []
    unreachable_hosts = []

    for host in hosts:
        try:
            result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', timeout=5)  # Timeout set to 5 seconds
            if result.returncode == 0:
                reachable_hosts.append(host)
            else:
                unreachable_hosts.append(host)
        except subprocess.TimeoutExpired:
            print(f"Timed out while pinging {host}")
            unreachable_hosts.append(host)
        except Exception as e:
            print(f"An error occurred while pinging {host}: {e}")
            unreachable_hosts.append(host)

    return reachable_hosts, unreachable_hosts


def get_ip_addresses(input_text):
    # Using regex to find IP addresses in the input text
    ip_addresses = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', input_text)
    return ip_addresses


if __name__ == "__main__":
    hosts_to_ping = []

    # Continuous input loop
    while True:
        user_input = input("Enter a host to ping (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        # Extract IP addresses from user input
        hosts_to_ping.extend(get_ip_addresses(user_input))

    reachable, unreachable = ping_hosts(hosts_to_ping)

    print("Reachable hosts:", reachable)
    print("Unreachable hosts:", unreachable)


import subprocess
import re


def ping_hosts(hosts, packet_count=1, timeout=5):
    reachable_hosts = {}
    unreachable_hosts = {}

    for host in hosts:
        try:
            result = subprocess.run(['ping', '-c', str(packet_count), '-W', str(timeout), host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', timeout=timeout)
            if result.returncode == 0:
                # Extracting average round-trip time (RTT) from ping output
                rtt_match = re.search(r'rtt min/avg/max/mdev = (\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)', result.stdout)
                avg_rtt = rtt_match.group(2) if rtt_match else 'N/A'
                reachable_hosts[host] = avg_rtt
            else:
                unreachable_hosts[host] = result.stderr.strip()
        except subprocess.TimeoutExpired:
            unreachable_hosts[host] = f"Timed out after {timeout} seconds"
        except Exception as e:
            unreachable_hosts[host] = f"An error occurred: {e}"

    return reachable_hosts, unreachable_hosts


def get_ip_addresses(input_text):
    # Using regex to find IP addresses in the input text
    ip_addresses = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', input_text)
    return ip_addresses


if __name__ == "__main__":
    hosts_to_ping = []

    # Continuous input loop
    while True:
        user_input = input("Enter a host to ping (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        # Extract IP addresses from user input
        hosts_to_ping.extend(get_ip_addresses(user_input))

    packet_count = int(input("Enter the number of packets to send per ping (default is 1): ") or 1)
    timeout = int(input("Enter the timeout duration in seconds (default is 5): ") or 5)

    reachable, unreachable = ping_hosts(hosts_to_ping, packet_count, timeout)

    print("\nReachable hosts:")
    for host, avg_rtt in reachable.items():
        print(f"{host}: Average RTT = {avg_rtt} ms")

    print("\nUnreachable hosts:")
    for host, error_message in unreachable.items():
        print(f"{host}: {error_message}")


import subprocess
import re
from collections import defaultdict
from colorama import init, Fore, Style


def ping_hosts(hosts, packet_count=1, timeout=5, repeat=1):
    reachable_hosts = defaultdict(list)
    unreachable_hosts = {}

    for host in hosts:
        for _ in range(repeat):
            try:
                result = subprocess.run(['ping', '-c', str(packet_count), '-W', str(timeout), host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', timeout=timeout)
                if result.returncode == 0:
                    # Extracting average round-trip time (RTT) from ping output
                    rtt_match = re.search(r'rtt min/avg/max/mdev = (\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)', result.stdout)
                    avg_rtt = rtt_match.group(2) if rtt_match else 'N/A'
                    reachable_hosts[host].append(float(avg_rtt))
                else:
                    unreachable_hosts[host] = result.stderr.strip()
            except subprocess.TimeoutExpired:
                unreachable_hosts[host] = f"Timed out after {timeout} seconds"
            except Exception as e:
                unreachable_hosts[host] = f"An error occurred: {e}"

    return reachable_hosts, unreachable_hosts


def get_ip_addresses(input_text):
    # Using regex to find IP addresses in the input text
    ip_addresses = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', input_text)
    return ip_addresses


def display_summary(reachable, unreachable):
    total_hosts = len(reachable) + len(unreachable)
    total_reachable = len(reachable)
    total_unreachable = len(unreachable)
    percent_reachable = (total_reachable / total_hosts) * 100 if total_hosts != 0 else 0

    print("\nSummary Statistics:")
    print(f"Total hosts: {total_hosts}")
    print(f"Reachable hosts: {total_reachable}")
    print(f"Unreachable hosts: {total_unreachable}")
    print(f"Percentage of reachable hosts: {percent_reachable:.2f}%")


def colorize(text, color):
    return f"{color}{text}{Style.RESET_ALL}"


if __name__ == "__main__":
    init(autoreset=True)  # Initialize colorama

    hosts_to_ping = []

    # Continuous input loop
    while True:
        user_input = input("Enter a host to ping (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        # Extract IP addresses from user input
        hosts_to_ping.extend(get_ip_addresses(user_input))

    packet_count = int(input("Enter the number of packets to send per ping (default is 1): ") or 1)
    timeout = int(input("Enter the timeout duration in seconds (default is 5): ") or 5)
    repeat = int(input("Enter the number of times to repeat pings per host (default is 1): ") or 1)

    reachable, unreachable = ping_hosts(hosts_to_ping, packet_count, timeout, repeat)

    print("\nReachable hosts:")
    for host, rtts in reachable.items():
        avg_rtt = sum(rtts) / len(rtts)
        color_host = colorize(host, Fore.GREEN)
        print(f"{color_host}: Average RTT = {avg_rtt:.2f} ms (based on {len(rtts)} ping(s))")

    print("\nUnreachable hosts:")
    for host, error_message in unreachable.items():
        color_host = colorize(host, Fore.RED)
        print(f"{color_host}: {error_message}")

    display_summary(reachable, unreachable)
