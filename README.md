# 🔐 Cybersecurity Portfolio

A personal cybersecurity portfolio showcasing network scanning scripts, CTF writeups, and security tools. This repository is organized to make it easy to find, run, and build upon each project.

## 📂 Repository Structure

```
Cybersecurity/
├── network-scanning/       # Scripts for network reconnaissance and port scanning
│   ├── port_scanner.py     # Basic TCP port scanner
│   └── README.md
├── ctf-writeups/           # Capture The Flag challenge writeups
│   ├── README.md
│   └── example/            # Placeholder for future CTF writeups
├── security-tools/         # Standalone security utilities and helpers
│   └── README.md
└── projects/               # Larger multi-file security projects
    └── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- No additional dependencies required for the basic scripts

### Running the Port Scanner

```bash
cd network-scanning
python port_scanner.py --host 127.0.0.1 --start-port 1 --end-port 1024
```

## 📁 Sections

### Network Scanning

Scripts for discovering open ports, running service fingerprinting, and mapping network topology. See [`network-scanning/README.md`](network-scanning/README.md) for details.

### CTF Writeups

Step-by-step solutions for Capture The Flag challenges across platforms such as Hack The Box, TryHackMe, and PicoCTF. See [`ctf-writeups/README.md`](ctf-writeups/README.md) for details.

### Security Tools

Standalone utilities for tasks like hash cracking, log analysis, and payload generation. See [`security-tools/README.md`](security-tools/README.md) for details.

### Projects

Larger, multi-file security projects and research. See [`projects/README.md`](projects/README.md) for details.

## ⚠️ Disclaimer

All tools and scripts in this repository are intended for **educational purposes and authorized testing only**. Do not use them against systems you do not own or have explicit permission to test. The author assumes no liability for misuse.

## 📄 License

This project is licensed under the terms of the [LICENSE](LICENSE) file.
