# 🧠 Linux Command System via SSH | Control a Remote OS From Your Terminal

> **"One Terminal to Rule Them All..."**  
> Remotely control another Linux operating system using your own — like a boss. 💻⚡

---

## 🚀 Overview

This Python-based tool allows you to **log into a remote Linux machine using SSH** and perform **real-time system operations** — all from your local terminal. Think of it as a **magic shell** that controls an entirely different OS without switching screens.

From **creating users**, to **editing files**, to **installing packages** — you name it, this script does it. 🧙‍♂️✨

---

## 🔧 Features

- 🔐 SSH-based login to any 192.168.\*.\* Linux machine
- 🗓️ View date, calendar, and system IP
- 📁 List files and their permissions
- 📄 Read, write, create, and delete files remotely
- 👤 Add or delete users
- 📦 Install packages using `yum`
- 🛡️ Modify file permissions for owner/group/others
- 🧠 Fully interactive CLI interface

---

## 🖥️ Demo

```bash
$ python ssh.py

Welcome to Linux Command System
~~.~~.~~.~~.~~.~~.~~.~~.~~.~~

What is your user name: root
What is your ip address (192.168.____): 1.101
What do u want Linux to perform (Type help for options): list
```

## 🧑‍💻 Tech Stack

- Python 3.x  
- SSH Protocol  
- `os.system()` module  
- Linux Terminal Commands  

---

## ⚙️ How It Works

1. Enter the username and IP address of the remote system.  
2. Choose what task you want to perform (e.g., list files, add user, write to file).  
3. The script executes the equivalent Linux command on the remote machine via SSH.  
4. Responses (like file lists or confirmations) are displayed on your terminal.  

---

## 🧪 Supported Commands  

> 💡 Type `help` inside the script for a full list.

---
