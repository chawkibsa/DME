![DME](https://user-images.githubusercontent.com/86046707/227709873-9e1dc9f8-5ed0-4ccf-800f-195f3c9b9ee1.png)
# DME
DME is a Python-based chat application that provides secure communication between users. This application uses Tkinter for GUI, Json for data serialization, sockets for network communication and threading for concurrent execution.

## Table of contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Security](#security)
- [Contributing](#contributing)
- [Demo](#demo)
- [License](#license)

## Prerequisites
To run the application, you will need to have Python 3 installed on your system. You can download and install the latest version of Python from the official website: https://www.python.org/downloads/.

## Installation
You can clone the repository to your local machine using the following command:
```
git clone https://github.com/Chawki-BS/DME.git
```
After cloning the repository, you need to install the required dependencies using the following command:
```
pip install -r requirements.txt
```

## Usage
To start the server, run the following command:
```
python3 server_login.py
```
You will see a server login page. Enter your IP address and a none used port number to start the server. 
To start the client, run the following command:
```
python3 main.py
```
You will see a client login page. Enter client name, server IP address and server port number to connect to the server.
- You can then invite other users to join the chatroom by sharing the chatroom IP address and port number with them and run the "main.py" file.
- You can then start chatting with other users in the chatroom.

## Features
- Secure and private chatroom.
- User authentication and registration.
- Real-time messaging using sockets and threading.
- Ability to administer the chatroom (kick and ban users).
- User-friendly interface using Tkinter.

## Security
- Access Control: Access to chatrooms is restricted to authorized users only. Certain actions, such as creating or deleting chatrooms, are restricted to administrators only.
- Testing: I have conducted security testing to identify and fix security vulnerabilities in the chatroom app. Automated tools are used to scan the app for vulnerabilities, and manual penetration testing is conducted to simulate attacks by an attacker.
- As we take security seriously, we are currently working on improving the app's security focusing on these features :
  - LDAP Server Integration: We are currently working on implementing an LDAP server to authenticate users using certificates that are signed by a certificate authority. This will provide an additional layer of security to our chatroom app by ensuring that only authorized users can access it.
  - Encryption: All chat messages and user credentials are encrypted using SSL/TLS certificate to protect their confidentiality during transmission.
  - Hashing: To ensure the integrity of data, we are implementing hashing algorithms to validate the authenticity of data transmitted between the client and server.

## Contributing 
If you find any bugs or issues with the app, please report them by opening an issue on Github. Contributions to the app are also welcome - if you have any ideas for new features or improvements, please feel free to submit a pull request.

## License 
This project is licensed under the MIT License - see the LICENSE file for details.
