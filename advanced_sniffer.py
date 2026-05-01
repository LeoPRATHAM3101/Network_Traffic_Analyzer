from scapy.all import rdpcap, IP, TCP, UDP
from analyzer_utils import detect_port_scan, get_top_ip, suspicious_ports

packets = rdpcap("sample_capture.pcap")

tcp_count = 0
udp_count = 0
ip_list = []
port_list = []
suspicious_hits = 0

print("Analyzing packets...\n")

for packet in packets:

    if packet.haslayer(IP):
        ip_list.append(packet[IP].src)

    if packet.haslayer(TCP):
        tcp_count += 1
        port_list.append(packet[TCP].dport)

        if packet[TCP].dport in suspicious_ports():
            suspicious_hits += 1

    elif packet.haslayer(UDP):
        udp_count += 1


# Results
print("Total Packets:", len(packets))
print("TCP Packets:", tcp_count)
print("UDP Packets:", udp_count)

# Top IP
top_ip = get_top_ip(ip_list)
print("\nMost Active IP:", top_ip)

# Port Scan Detection
if detect_port_scan(port_list):
    print("\n🚨 Possible Port Scanning Detected!")
else:
    print("\nNo Port Scanning Detected")

# Suspicious Ports
print("\nSuspicious Port Hits:", suspicious_hits)
