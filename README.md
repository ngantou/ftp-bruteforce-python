# 🔐 FTP Brute-Force Tool in Python

This is a simple brute-force tool for FTP written in Python.
It uses `ftplib` to test combinations of usernames and passwords from dictionary files against a remote FTP server.

> ⚠️ **Disclaimer:** This tool is intended **only** for educational purposes and authorized penetration testing. **Do not use it on systems you do not own or have explicit permission to test.**

---

## 📦 Repository Name

**ftp-bruteforce-python**

## 📝 Description

Brute-force FTP tool written in Python using `ftplib`, allowing login/password dictionary attacks on an FTP service — for educational or authorized testing only.

---

## 📁 Project Structure

ftp-bruteforce-python/
├── ftp_bruteforce.py # The main script
├── users.txt # Sample usernames list
├── passwords.txt # Sample passwords list
└── README.md # Project documentation


---

## ⚙️ Requirements

- Python 3.x
- Standard Python library only (no external packages required)

---

## 🚀 Usage

### 🧪 Test login/passwords on an FTP server:

```bash
python ftp_bruteforce.py -c <TARGET_IP> -l users.txt -p passwords.txt


## 👨‍💻 Author

Made with ❤️ by [NgantouJoël]
Contributions and suggestions are welcome!