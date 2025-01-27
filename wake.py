import socket
import argparse

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
        print(f"Magic packet sent to {mac_address}")
    else:
        print("Invalid MAC address format")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wake on LAN script')
    parser.add_argument('mac_address', type=str, help='MAC address of the device to wake')
    args = parser.parse_args()

    wake_on_lan(mac_address=args.mac_address)
