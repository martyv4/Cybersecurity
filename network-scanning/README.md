# Network Scanning

This folder contains Python scripts for network reconnaissance and port scanning.

## Scripts

| Script | Description |
|--------|-------------|
| `port_scanner.py` | Basic multi-threaded TCP port scanner |

## Usage

### port_scanner.py

Scans a range of TCP ports on a target host and prints which ports are open, along with the associated service name when known.

```bash
python port_scanner.py --host <target> --start-port <int> --end-port <int>
```

**Options:**

| Flag | Default | Description |
|------|---------|-------------|
| `--host` | *(required)* | Target hostname or IP address |
| `--start-port` | `1` | First port in the scan range |
| `--end-port` | `1024` | Last port in the scan range (inclusive) |
| `--timeout` | `0.5` | TCP connection timeout in seconds |
| `--workers` | `100` | Number of concurrent scanning threads |

**Example — scan localhost ports 1–1024:**

```bash
python port_scanner.py --host 127.0.0.1 --start-port 1 --end-port 1024
```

**Example output:**

```
[*] Scanning 127.0.0.1 (127.0.0.1) — ports 1–1024
[+] Open ports on 127.0.0.1:
    22/tcp  —  ssh
    80/tcp  —  http
    443/tcp —  https
[*] Scan complete. 3 open port(s) found.
```

## ⚠️ Legal Notice

Only run these scripts against hosts you own or have **explicit written permission** to test.
