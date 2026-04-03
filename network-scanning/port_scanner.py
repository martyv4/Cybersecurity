#!/usr/bin/env python3
"""
Basic TCP Port Scanner

Scans a range of TCP ports on a target host and reports which ports are open.

Usage:
    python port_scanner.py --host <target> --start-port <int> --end-port <int> [--timeout <float>]

Example:
    python port_scanner.py --host 127.0.0.1 --start-port 1 --end-port 1024

WARNING: Only scan hosts you own or have explicit written permission to test.
"""

import argparse
import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed


def scan_port(host: str, port: int, timeout: float) -> tuple[int, bool]:
    """Attempt a TCP connection to host:port. Returns (port, is_open)."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return port, True
    except (ConnectionRefusedError, socket.timeout, OSError):
        return port, False


def run_scan(host: str, start_port: int, end_port: int, timeout: float, max_workers: int = 100) -> list[int]:
    """Scan ports in [start_port, end_port] on host concurrently. Returns sorted list of open ports."""
    open_ports: list[int] = []
    ports = range(start_port, end_port + 1)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(scan_port, host, port, timeout): port for port in ports}
        for future in as_completed(futures):
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)

    return sorted(open_ports)


def resolve_host(host: str) -> str:
    """Resolve hostname to IP address."""
    try:
        return socket.gethostbyname(host)
    except socket.gaierror as exc:
        print(f"[!] Could not resolve host '{host}': {exc}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Basic TCP port scanner",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--host", required=True, help="Target hostname or IP address")
    parser.add_argument("--start-port", type=int, default=1, help="First port to scan")
    parser.add_argument("--end-port", type=int, default=1024, help="Last port to scan (inclusive)")
    parser.add_argument("--timeout", type=float, default=0.5, help="Connection timeout in seconds")
    parser.add_argument("--workers", type=int, default=100, help="Number of concurrent threads")
    args = parser.parse_args()

    if not (1 <= args.start_port <= 65535) or not (1 <= args.end_port <= 65535):
        print("[!] Port numbers must be between 1 and 65535.", file=sys.stderr)
        sys.exit(1)
    if args.start_port > args.end_port:
        print("[!] --start-port must be less than or equal to --end-port.", file=sys.stderr)
        sys.exit(1)

    ip = resolve_host(args.host)
    print(f"[*] Scanning {args.host} ({ip}) — ports {args.start_port}–{args.end_port}")

    open_ports = run_scan(ip, args.start_port, args.end_port, args.timeout, args.workers)

    if open_ports:
        print(f"\n[+] Open ports on {args.host}:")
        for port in open_ports:
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "unknown"
            print(f"    {port}/tcp  —  {service}")
    else:
        print("\n[-] No open ports found in the specified range.")

    print(f"\n[*] Scan complete. {len(open_ports)} open port(s) found.")


if __name__ == "__main__":
    main()
