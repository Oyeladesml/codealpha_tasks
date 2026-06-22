# CodeAlpha Cybersecurity Internship Portfolio

## Task 1: Basic Network Sniffer

### 🔍 Project Overview
This project is a lightweight, raw network packet sniffer built using Python and the `scapy` library. The script captures live network traffic passing through the designated local interface, unpacks the layer headers, and decodes vital network telemetry data in real-time. It serves as a fundamental security engineering tool for traffic analysis and network troubleshooting.

### 🛠️ Core Features Implemented
* **Live Ingestion:** Continuously hooks into the specified network interface card to read raw frame boundaries.
* **Protocol Extraction:** Inspects the layer-3 IP header to identify active transport and control protocols (e.g., Protocol 1 for ICMP, Protocol 6 for TCP, Protocol 17 for UDP).
* **Address Mapping:** Extracts and clearly maps absolute Source and Destination IPv4 addresses to map data flows.
* **Safety Control:** Configured with specific packet capture caps to manage system memory overhead during standard analytical sessions.

### 💻 System Prerequisites & Setup

1. **Environment:** Run inside a Linux environment (such as Kali Linux) with root/administrative privileges to allow raw socket access.
2. **Dependencies:** Ensure Python 3 and the `scapy` packet engineering library are installed:
   ```bash
   pip install scapy
