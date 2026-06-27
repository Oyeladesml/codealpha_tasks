# CodeAlpha Cybersecurity Internship Portfolio

## Task 4: Network Intrusion Detection System (IDS) Implementation

### 🛡️ Project Overview
This project involves deploying and configuring **Snort 3** (Snort++), an open-source Network Intrusion Detection System (NIDS), inside a Kali Linux environment. The setup monitors a local network interface in passive mode, parsing traffic signatures in real-time to alert administrative personnel of potential protocol anomalies and network policy violations.

### 🛠️ Core Features Implemented
* **Signature-Based Detection:** Configured custom local rules to intercept explicit ICMP (Ping) traffic blocks traveling across the segment.
* **Lua Configuration Integration:** Successfully migrated and integrated user-defined rules directly into the modern Snort 3 configuration structure (`snort.lua`).
* **Console Logging Mode:** Deployed the detection engine using the fast-alert mode (`-A alert_fast`) to output immediate threat notifications directly to the live analyst console.

📥 Snort 3 Installation Guide
To get Snort 3 up and running on Kali Linux, execute the following commands to install the engine and its required dependencies:
# Update your system package manager
sudo apt update && sudo apt upgrade -y

# Install the Snort 3 core package and standard ruleset
sudo apt install snort snort-rules-default -y

# Verify the installation was successful
snort -V

### 📝 Custom Detection Rule Architecture
### The signature implemented to track protocol anomalies utilizes the following structure inside `/etc/snort/rules/local.rules`:
`alert icmp any any -> any any (msg:"ICMP Packet Detected via Snort"; sid:1000001; rev:1;)'


 ### 🚀 Execution & Verification Command
To launch Snort 3 live and bind it to the primary interface to process incoming packets, run:
sudo snort  -R /etc/snort/rules/local.rules -i eth0 -A alert_fast

🧠 Key Concepts Learned
NIDS Engine Architecture: Gained hands-on experience dealing with the structural configuration changes between legacy engines and modern Snort 3 rule linking.
Traffic Baseline Analysis: Developed practical skills in observing how deep packet inspection identifies and logs signatures to maintain network visibility.
