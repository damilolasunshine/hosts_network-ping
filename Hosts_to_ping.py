import subprocess


def ping_hosts(hosts):
    reachable_hosts = []
    unreachable_hosts = []

    for host in hosts:
        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                encoding='utf-8')
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
