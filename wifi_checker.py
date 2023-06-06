import socket

def is_wifi_connected():
    try:
        # Create a TCP/IP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)  # Set a timeout value for the connection

        # Connect to a remote server using a common website address
        s.connect(("www.google.com", 80))

        # Connection successful
        s.close()
        return True
    except socket.error:
        # Connection failed
        return False

# Check if device is connected via Wi-Fi
if is_wifi_connected():
    print("Device is connected to Wi-Fi.")
else:
    print("Device is not connected to Wi-Fi.")
