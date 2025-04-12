CTF HOW TO

# HARDWARE
- ESP32 chip board
- How to connect to an ESP32 chip board through UART.
- Serial connection through the USB port (micro USB / type C) if it has a FTDI chip (USB to serial).
- Pin out ESP32 chip: connect to Rx, Tx, and Ground (or IO, GPIO, and Ground) using a UART to USB cable.
- After plugged in, in Terminal run either:
  - Picocom (example: `picocom /dev/ttyUSB0 -b 115200`)
  - Esptool
  - Putty
  - Screen
  - Arduino IDE
  - Minicom
- Helpful notes:
  - Common baud rates: 9600, 1200, 2400, 4800, 19200, 38400, 57600, and 115200 bps.
  - To find ports: run `lsusb` or `ls /dev/tty*`

## Memory
- Command to dump 4MB of flash:
  ```bash
  python3 -m esptool --port /dev/ttyUSB0 -b 9600 read_flash 0 0x400000 flashdump.bin
  ```
- Tools:
  - Esptool
  - Binwalk (analyze flashdump)
  - Strings (view readable text in binaries)
  - Ghidra
  - GHex

# WEB
- Curl (web requests)
- Burp Suite
- ffuf (URL fuzzing)

# RF
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

# Forensics
(Section to be expanded)

# PWN
(Section to be expanded)

# STEGANOGRAPHY
- Images
(Section to be expanded)

# CAR
- [TruckDevil GitHub](https://github.com/LittleBlondeDevil/TruckDevil)
- [Awesome CANbus GitHub](https://github.com/iDoka/awesome-canbus)

# Helpful notes and tools
- Audacity
- Wireshark
- Arduino IDE
- Ghidra
- Burp Suite
- Putty
- GHex

# Helpful Links
- https://medium.com/quiknapp/fuzz-faster-with-ffuf-c18c031fc480
- https://cantreally.cyou/
- https://www.dcode.fr/
- https://gchq.github.io/CyberChef/
- https://python-can.readthedocs.io/en/stable/
- https://github.com/iDoka/awesome-canbus

# Setup Instructions
## General Tools
- Install Python3, Pip, Pwntools
- CANBus utils: `can-utils`, `python-can`
- Visual Studio Code setup (official Microsoft repository)

## Hardware Tools
- Picocom
- Esptool
- Putty
- Screen
- Minicom
- Binwalk
- Ghidra (Manual or Snap installation)
- GHex

## Web Tools
- Burp Suite

## Wireless Tools
- Wireshark

## Java Development Kit (JDK 17)
- Install OpenJDK or Oracle JDK

## Wine
- Install Wine for Windows compatibility

# Linux Commands Commonly Used by Hackers
- `ls`, `cd`, `pwd`, `cp`, `mv`, `rm`, `find`, `cat`, `nano/vim`, `chmod`, `chown`, `ping`, `ifconfig/ip`, `netstat`, `nmap`, `whois`, `dig`, `traceroute`, `ssh`, `scp`, `ps`, `top/htop`, `kill`, `pkill`, `bg/fg`, `uname -a`, `df`, `du`, `uptime`, `free`, `history`, `tar`, `gzip/gunzip`, `zip/unzip`, `wget`, `curl`, `grep`, `sed`, `awk`, `cut`, `sort`, `uniq`, `iptables`, `tcpdump`, `openssl`, `metasploit`, `hydra`, `john`, `aircrack-ng`

# CTF SPECIFIC
## HTH
(Section to be expanded)

## SHMOOCON Steganography
- Layered QR code reconstruction
- STL file
  - Load in Blender
  - Render light hitting it
- AWS
- PCAP Analysis
- Docker

## Hack-A-Sat
(Section to be expanded)

## THOTCON
- Crypto challenges (ROT13, Binary decoding, Base64, Caesar cipher)
- RF (Morse code signal identification)
- Badge (Memory dumps, strings extraction)

## Battelle Cyber Challenges
- Reverse Engineering: Device firmware analysis, STL files, mystery devices.
- Binary Exploitation: ROP chains, chatbot bypass.
- Forensics / Crypto: Holiday-themed forensics challenges.
- Multi-Architecture Shellcode: Cross-architecture exploits.

# Logic Analyzer Example (I2C Transactions)
```
I2C    start    5.78338656    ...
I2C    address  5.78339712    ...
I2C    data     5.78352432    ...
...
```

---

*This document is a work in progress for CTF hardware, software, and general setup guidance.*

