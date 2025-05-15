import socket

NAO_IP = "172.18.16.31"  # Replace with NAO's IP
NAO_PORT = 5005

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send 'start' command
message = "start"
sock.sendto(message.encode(), (NAO_IP, NAO_PORT))
print("Sent start command to NAO.")

sock.close()
