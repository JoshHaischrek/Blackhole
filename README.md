# Blackhole.py

[![Python Version](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Easy way to update the hostfile on Windoww or Unix systems to resolve FQDN to 0.0.0.0
Note: This Module only functions as Admin/Root so if you encounter errors when running, ensure you are elevated before other troubleshooting steps. 

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Examples](#examples)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)

---

## Features/

- **MAKE SURE YOU RUN THIS AS ADMIN** In order to edit the hostfile, this module needs to be run as administrator/root. That means whatever you import this into needs to also be run as Admin to utilize this
- **Checks your OS**: Check's your os to determine the host file location
- **Adds a user submited FQDN to the hostfile**:Allows a user to type in a fqdn to resolve to 0.0.0.0
- **Modify exsisting host file entries**: If a duplicate entry is submited, the module will recognize it and allow you to moify or delete the entry


---

## Installation
clone the repository and install locally:

```bash
git clone https://github.com/JoshHaischrek/Blackhole.git
cd Blackhole
pip install .
```

---

## Usage


```python
- Run the module as a script (python3 blackhole.py).
- Run the module as a module (python3 -m blackhole).
---

## Examples

You could add this module is as a part of a larger program, allowing you to access and blackhole a designated FQDN. This could be useful for testing webservers, server certificates or security. For example you could create a program that mimics a favorites bar. The user enters a FQDN for what they want added to favorits, and it instead, adds it to the host file and stops it being resolved.

---

### Acknowledgments

Thanks for a great final year, and For putting up with us Professor! (Also thanks to stack overflow for the assist with the FileNotFoundError. I completly forgot about try/except from the previous labs, and https://www.makeareadme.com for the template for this readme. Never used MD language and wanted it to be properly formated.
