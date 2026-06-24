# CodeAlpha Cybersecurity Internship Portfolio

## Task 1: Basic Network Sniffer

## 🔍 Project Overview
This project is a lightweight, raw network packet sniffer built using Python and the `scapy` library. The script captures live network traffic passing through the designated local interface, unpacks the layer headers, and decodes vital network telemetry data in real-time. It serves as a fundamental security engineering tool for traffic analysis and network troubleshooting.

### 🛠️ Core Features Implemented
Live Ingestion: Continuously hooks into the specified network interface card to read raw frame boundaries.
Protocol Extraction: Inspects the layer-3 IP header to identify active transport and control protocols (e.g., Protocol 1 for ICMP, Protocol 6 for TCP, Protocol 17 for UDP).
Address Mapping: Extracts and clearly maps absolute Source and Destination IPv4 addresses to map data flows.
Safety Control: Configured with specific packet capture caps to manage system memory overhead during standard analytical sessions.

### 💻 System Prerequisites & Setup

1. Environment: Run inside a Linux environment (such as Kali Linux) with root/administrative privileges to allow raw socket access.
2. Dependencies: Ensure Python 3 and the `scapy` packet engineering library are installed:
   ```bash
   pip install scapy
   

🚀 Execution Instructions
Run the script using sudo to grant the necessary network interface access permissions:
```bash
sudo python3 sniffer.py

```
📊 Sample Output Reference
When traffic crosses the interface, the engine decodes and outputs data packets in the following structured format:
```text
[*] Starting Basic Network Sniffer... Press Ctrl+C to stop.
[+] Packet: Source IP: 10.0.2.15 --> Destination IP: 8.8.8.8 | Protocol: 1
[+] Packet: Source IP: 8.8.8.8 --> Destination IP: 10.0.2.15 | Protocol: 1
[+] Packet: Source IP: 10.0.2.15 --> Destination IP: 192.168.1.1 | Protocol: 17
[+] Packet: Source IP: 142.250.179.238 --> Destination IP: 10.0.2.15 | Protocol: 6
