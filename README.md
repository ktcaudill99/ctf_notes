# CTF HOW-TO: A Practical Guide for Cybersecurity Challenges

## 📦 Table of Contents
- [Hardware](#hardware)
- [Web Tools](#web-tools)
- [RF Tools](#rf-tools)
- [Forensics](#forensics)
- [PWN](#pwn)
- [Steganography](#steganography)
- [Car Hacking](#car-hacking)
- [Helpful Notes & Links](#helpful-notes--links)
- [Setup & Installation](#setup--installation)
- [CTF Specific Challenges](#ctf-specific-challenges)

---

## 🔌 Hardware
### ESP32 Chip Board
Connect using UART via USB (micro USB or Type-C if it has an FTDI chip).
- **Common Baud Rates**: 9600, 115200, etc.
- **Tools**: `picocom`, `esptool`, `putty`, `screen`, `minicom`, `Arduino IDE`
- **Port Discovery**: `lsusb` or `ls /dev/tty*`

### Memory Dumping
- Dump flash:
```bash
python -m esptool --port COM5 -b 115200 read_flash 0 0x400000 flashdump.bin
```
- Analyze with: `binwalk`, `strings`, `Ghidra`, `GHex`

---

## 🌐 Web Tools
- `curl`: Command-line web request tool
- `Burp Suite`: Intercepting proxy tool for web security testing
- `ffuf`: Fuzzing web applications (https://medium.com/quiknapp/fuzz-faster-with-ffuf-c18c031fc480)

---

## 📡 RF Tools
- GQRX, Universal Radio
- Apps: nRF Connect, Flipper, AirGuard, Aruba Utilities, WiFiman, Meshtastic, goTenna, Zello

---

## 🧪 Forensics
- Tools: `Wireshark`, `Audacity`, `Ghidra`, `strings`, `CyberChef`

---

## 🧨 PWN
- Install `pwntools`: `python3 -m pip install --upgrade pwntools`
- Practice with ROP chains, binary analysis, shellcode injection

---

## 🖼️ Steganography
- Analyze images: [Aperi'Solve](https://www.aperisolve.com/)
- Tools: `zsteg`, `steghide`, `binwalk`, `GIMP`, `exiftool`

---

## 🚗 Car Hacking
- Repos:
  - https://github.com/LittleBlondeDevil/TruckDevil
  - https://github.com/iDoka/awesome-canbus
- Tools: `python-can`, `can-utils`

---

## 🛠️ Helpful Notes & Links
### Tools:
- `Ghidra`, `Burp Suite`, `Putty`, `GHex`, `Audacity`, `Arduino IDE`

### Useful Links:
- https://dcode.fr/
- https://gchq.github.io/CyberChef/
- https://python-can.readthedocs.io/en/stable/
- https://cantreally.cyou/

---

## ⚙️ Setup & Installation
### System Prep:
```bash
sudo apt update && sudo apt install python3 python3-pip
```

### Tools:
- `Pwntools`: See [PWN](#pwn)
- `CANBus`: `sudo apt install can-utils`, `pip install python-can`
- `Visual Studio Code`: Follow [Microsoft instructions](https://code.visualstudio.com/docs/setup/linux)
- `Picocom`, `Esptool`, `Putty`, `Screen`, `Minicom`, `Binwalk`, `Ghex`: Use `apt install` commands as listed in the original document
- `Ghidra`: Use JDK 17; install from snap or manually configure desktop launcher

---

## 🎯 CTF Specific Challenges
### HTH

### SHMOOCON
- **Steganography**:
  - Layered QR code reconstruction
  - STL file → Blender render
  - AWS bucket analysis
  - PCAP file analysis
  - Dockerized environments

### HACK-A-SAT

### THOTCON
- **Crypto Examples**:
  - ROT13, Caesar Cipher, Bacon’s Cipher, Base64
  - Morse decoding from RF capture
- **Badge Challenge**:
  - Dump and search flash memory for flags using `esptool`, `strings`

### BATTELLE Cyber Challenge
- Reverse Engineering
- Binary Exploitation
- Forensics & Crypto
- Multi-Architecture Shellcode

### Logic Analyzer Sample Output
- Use for debugging I2C communication or similar

---

## 📍 Car Hacking Village 2024
More updates to come...

---

> *This README is a living document. Feel free to contribute or adapt it for your CTF team’s toolkit.*

