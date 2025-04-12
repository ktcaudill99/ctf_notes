# CTF HOW TO

## HARDWARE
- **ESP32 Chip Board**
  - Connect via UART.
  - Serial connection through USB port (Micro USB / Type C) if FTDI chip is present.
  - Pinout ESP32: Connect to Rx, Tx, Ground (or IO, GPIO, Ground) using a UART to USB cable.
  - After connection, use tools like:
    - Picocom (`picocom /dev/ttyUSB0 -b 115200` or `picocom /dev/ttyUSB0 -b 9600`)
    - Esptool
    - Putty
    - Screen
    - Arduino IDE
    - Minicom
  - **Helpful notes:**
    - Common baud rates: 9600, 1200, 2400, 4800, 19200, 38400, 57600, 115200 bps.
    - Find ports in use: `lsusb` or `ls /dev/tty*`

### Memory Operations
- Dump 4MB of flash:
  ```bash
  python3 -m esptool --port /dev/ttyUSB0 -b 9600 read_flash 0 0x400000 flashdump.bin
  ```
- Tools:
  - Esptool
  - Binwalk
  - Ghidra
  - GHex
  - Strings (`strings flashdump.bin`)

## WEB
- Curl (Web requests)
- Burp Suite
- ffuf (URL fuzzing)

## RF
- GQRX
- Universal Radio
- ZeroChaos apps (fox hunt, etc.)
- nRF Connect
- Flipper
- AirGuard
- Aruba Utilities
- WiFi Analyzer
- WiFiman
- Meshtastic
- goTenna
- Zello

## FORENSICS
(Section to be expanded)

## PWN
(Section to be expanded)

## STEGANOGRAPHY
- Images
(Section to be expanded)

## CAR
- [TruckDevil GitHub](https://github.com/LittleBlondeDevil/TruckDevil)
- [Awesome CANbus GitHub](https://github.com/iDoka/awesome-canbus)

## Helpful Notes and Tools
- Audacity
- Wireshark
- Arduino IDE
- Ghidra
- Burp Suite
- Putty
- GHex

## Helpful Links
- [Fuzz Faster with ffuf](https://medium.com/quiknapp/fuzz-faster-with-ffuf-c18c031fc480)
- [cantreally.cyou](https://cantreally.cyou/)
- [Dcode Tools](https://www.dcode.fr/)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [Python CAN Documentation](https://python-can.readthedocs.io/en/stable/)
- [Awesome CANbus Collection](https://github.com/iDoka/awesome-canbus)

## Setup Instructions
### General Tools
- Install Python3
- Install Pwntools
- Install CANBus utils (`can-utils`, `python-can`)
- Install Visual Studio Code

### Hardware Tools
- Install Picocom
- Install Esptool
- Install Putty
- Install Screen
- Install Minicom
- Install Binwalk
- Install Ghidra (manual or Snap install)
- Install GHex

### Web and Wireless Tools
- Install Burp Suite
- Install Wireshark

### JDK 17 Installation
- Install OpenJDK or Oracle JDK 17

### Wine Installation
- Install Wine for Windows compatibility

## Linux Commands Commonly Used by Hackers
1. `ls`: Lists directory contents.
2. `cd`: Changes directory.
3. `pwd`: Shows the current directory.
4. `cp`: Copies files and directories.
5. `mv`: Moves or renames files.
6. `rm`: Removes files or directories.
7. `find`: Searches for files in directories.
8. `cat`: Concatenates and displays file contents.
9. `nano / vim`: Edits files within the command line.
10. `chmod`: Changes file permissions.
11. `chown`: Changes file owner and group.
12. `ping`: Tests connectivity to other IPs or domains.
13. `ifconfig` or `ip`: Displays network interfaces and configurations.
14. `netstat`: Shows network connections, routing tables, and interface statistics.
15. `nmap`: Scans networks and discovers hosts and services.
16. `whois`: Retrieves domain information.
17. `dig`: Resolves DNS queries.
18. `traceroute`: Traces the path packets take to reach a host.
19. `ssh`: Connects to remote machines via Secure Shell.
20. `scp`: Securely copies files between hosts.
21. `ps`: Displays current processes.
22. `top / htop`: Provides a real-time view of system processes.
23. `kill`: Terminates a process by its ID.
24. `pkill`: Kills processes by name.
25. `bg and fg`: Manages jobs in the background and foreground.
26. `uname -a`: Displays system information.
27. `df`: Shows disk space usage.
28. `du`: Checks directory space usage.
29. `uptime`: Displays system uptime.
30. `free`: Shows memory usage.
31. `history`: Shows command history.
32. `tar`: Archives files.
33. `gzip / gunzip`: Compresses and decompresses files.
34. `zip / unzip`: Creates and extracts zip files.
35. `wget`: Downloads files from the internet.
36. `curl`: Transfers data between servers.
37. `grep`: Searches for specific strings.
38. `sed`: Edits streams of text.
39. `awk`: Processes and reports on text data.
40. `cut`: Cuts out sections from files.
41. `sort`: Sorts lines of text files.
42. `uniq`: Finds unique lines.
43. `iptables`: Manages firewall rules.
44. `tcpdump`: Captures network packets.
45. `openssl`: Toolkit for secure communication.
46. `chmod`: Changes permissions.
47. `metasploit`: Penetration testing framework.
48. `hydra`: Brute-force tool for protocols.
49. `john`: Password cracker.
50. `aircrack-ng`: Wi-Fi network security assessment.

## CTF SPECIFIC
### HTH
(Section to be expanded)

### SHMOOCON Steganography
- Layered QR code reconstruction
- STL file: Load into Blender, render light
- AWS & PCAP analysis
- [Shmoocon Steganography Writeup](https://cantreally.cyou/posts/shmoocon-shmooganography/)
- Docker usage

### HACK-A-SAT
(Section to be expanded)

### THOTCON Challenges
#### Crypto
- Find the flag in the text string: `f33_qn_E0G`
  - Hint: Rot & Decay
  - Apply ROT13
  - **flag{s33_da_R0t}**
- Find the flag hidden in binary: `01100010010_01001310011101100_00001400010001100_0101000101010111`
  - It's binary but in a weird format.
  - **flag{n0t_k3v1n_b4c0n_l0lz}**
- Decode the Base64 string: `'RmxhZ3tiYXNlNjRfaXNfZWFzeX0='`
  - Base64 encoded.
  - **flag{base64_is_easy}**
- Decrypt the Caesar cipher: `Ykj pynih fgl iak weru tlmt utut hor dp oyu ytd? Smisu nn ia eeco ayhc sr heme.`
  - **flag{so1o_t0_so_n0k}**

#### RF
- Find the signal transmitting on 99.1 FM.
- Decode Morse code to **m0rs3c0d3**.

#### Badge
- Use Esptool to dump memory.
- View strings to find:
  - **flag{welcome_to_the_8bit_world}**
  - **flag{lets_fight!}**

### BATTELLE Cyber Challenges
- Reverse Engineering: Firmware recovery, device documentation analysis
- Binary Exploitation: ROP chains, chatbot bypassing
- Forensics / Crypto: Holiday-themed bandit investigations, treasure portal cracking
- Multi-Architecture Shellcode: Cross-architecture decoding

## Logic Analyzer Example (I2C Transactions)
```
I2C    start    5.78338656    1.60000001e-07
I2C    address  5.78339712    0.00012096    true    0x1F    false
I2C    data     5.78352432    0.00010976    true    0x42
...
```

---

*This document is a comprehensive guide for CTF hardware, software, and general setup guidance.*
