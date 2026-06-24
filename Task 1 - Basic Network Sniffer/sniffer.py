import scapy.all as scapy
def packet_callback(packet):
	# Check if the packet has an IP layer
	if packet.haslayer(scapy.IP):
		src_ip = packet[scapy.IP].src
		dst_ip = packet[scapy.IP].dst
		proto = packet[scapy.IP].proto
		
		print(f"[+] Packet: Source IP: {src_ip} -->Destination IP: {dst_ip} | Protocol: {proto}")

print("[*] Starting Basic Network Sniffer... Press Ctrl+C to stop.")
# Sniff traffic on your interface (adjust 'eth0' if yours is different)
scapy.sniff(iface="eth0", store=False,
prn=packet_callback, count=200)
