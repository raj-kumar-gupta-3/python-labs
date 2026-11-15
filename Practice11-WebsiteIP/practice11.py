import socket

website = input("Enter a website name (example: google.com): ")

try:
    ip = socket.gethostbyname(website)
    print("Website:", website)
    print("IP address:", ip)
except socket.gaierror:
    print("Could not find this website.")
