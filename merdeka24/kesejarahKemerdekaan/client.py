import socket
import sys
import re
import time

def main():
    one_time = 0
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_ip> <server_port>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_ip, server_port))
        print(f"Connected to {server_ip}:{server_port}")

        data = 'Request here'
        client_socket.sendall(data.encode() + b'\n')

        # Receive and print the server's response
        while True:
            one_time += 1
            if one_time >= 3:
                break
            response = client_socket.recv(4096)
            if not response:
                break
            print(response.decode(), end='')

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("\nConnection closed.")

if __name__ == "__main__":
    #adjust the code
    main()