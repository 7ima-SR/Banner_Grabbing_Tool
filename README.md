# 🛡️ Banner Grabbing Tool

A simple yet powerful Python-based banner grabbing tool to identify services running on open ports. Useful for network reconnaissance, penetration testing, and learning.

![Built With](https://img.shields.io/badge/Built%20With-Python-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Author](https://img.shields.io/badge/Author-Hima-red?style=flat-square)

---

## 🚀 Features

- Grab banners from single or multiple ports.
- Works with domain names or IP addresses.
- Custom timeout settings.
- Saves results to a file.
- Colorful CLI with ASCII art header.
- Error handling for timeouts and unreachable hosts.

---

## 📦 Requirements

Install the required libraries:

```bash
pip install termcolor pyfiglet
```

---

## 🧠 Usage

```bash
python banner_grabber.py -t <target> -p <ports> -T <timeout> -o <output_file>
```

---

## ✅ Arguments:

| Option        | Description                                      | Example                 |
|---------------|--------------------------------------------------|-------------------------|
| `-t, --target`| Target IP or domain (required)                   | `-t 192.168.1.1`        |
| `-p, --ports` | Ports to scan (comma-separated)                  | `-p 21,22,80,443`       |
| `-T, --timeout`| Timeout for each port (default: 1 second)       | `-T 2`                  |
| `-o, --output`| File to save banners (default: results_banner_grabbing.txt) | `-o my_results.txt` |

---

## 🔍 Example

```bash
python banner_grabber.py -t example.com -p 21,22,80,443 -T 2 -o banners.txt
```

---

## ⚠️ Disclaimer

- This project is for educational purposes only. Do not use these implementations in production or real-world security systems. They lack the security protections of real cryptographic libraries.

---

## 📜 License

This project is licensed under the MIT License.

---

## 📧 Contact

- Made with ❤️ by 7ima-SR
- Website:https://ibrahim-elsaied.netlify.app/

