from flask import Flask, render_template
from datetime import datetime

import os
import socket
import subprocess

# Configure the below
MAC_ADDRESS = os.getenv('PC_MAC_ADDRESS', 'default_mac_address')
PASSWORD = os.getenv('PC_PASSWORD', 'default_password')
REMOTE = os.getenv('PC_REMOTE', 'default_remote')

app = Flask(__name__)

@staticmethod
def wake_on_lan(mac_address):
    # Check if the MAC address is valid
    if len(mac_address) == 17 and mac_address.count(':') == 5:
        # Create a magic packet
        mac_address = mac_address.replace(':', '')
        data = bytes.fromhex('FF' * 6 + mac_address * 16)

        # Send the magic packet to the broadcast address
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(data, ('255.255.255.255', 9))
        print(f"{datetime.now()} - Magic packet sent to {mac_address}")
    else:
        print(f"{datetime.now()} - Invalid MAC address format")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/turnon')
def turnon():
    wake_on_lan(MAC_ADDRESS)
    return "Turned on PC"

@app.route('/shutdown')
def shutdown():
    subprocess.call(['sshpass', '-p', PASSWORD, 'ssh', REMOTE, 'shutdown /s /f /t 0'])
    print(f"{datetime.now()} - Turned off PC")
    return "Turned off PC"

@app.route('/restart')
def restart():
    subprocess.call(['sshpass', '-p', PASSWORD, 'ssh', REMOTE, 'shutdown /r /f /t 0'])
    print(f"{datetime.now()} - Restarting PC")
    return "Restarting PC"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
