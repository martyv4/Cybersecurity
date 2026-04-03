# CTF Writeups

This folder contains Capture The Flag (CTF) writeups — step-by-step solutions explaining how each challenge was solved.

## Structure

Each challenge gets its own subfolder named after the platform and challenge:

```
ctf-writeups/
├── example/               # Template / placeholder writeup
└── <platform>-<challenge>/
    ├── README.md          # Writeup (tools used, steps, flags)
    └── files/             # Supporting scripts or screenshots
```

## Platforms

Writeups will cover challenges from:

- [Hack The Box](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)
- [PicoCTF](https://picoctf.org/)
- [CTFtime](https://ctftime.org/)

## Adding a New Writeup

1. Create a new subfolder: `<platform>-<challenge-name>/`
2. Add a `README.md` with:
   - Challenge name and platform
   - Difficulty rating
   - Category (Web, Pwn, Crypto, Forensics, etc.)
   - Tools used
   - Step-by-step solution
   - Flag (if permitted to publish)
3. Add any supporting scripts or screenshots in a `files/` subfolder.
