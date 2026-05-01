from collections import Counter

def detect_port_scan(port_list):
    unique_ports = len(set(port_list))
    if unique_ports > 20:
        return True
    return False


def get_top_ip(ip_list):
    counter = Counter(ip_list)
    return counter.most_common(1)


def suspicious_ports():
    return [21, 22, 23, 3389, 445]  # FTP, SSH, Telnet, RDP, SMB
