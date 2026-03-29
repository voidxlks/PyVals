import socket
import threading
import pickle

HOST = "127.0.0.1"  # change to your server IP later
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
    print("Connected to server!")
except:
    print("Connection failed.")
    exit()

# Player state
player_data = {
    "x": 100,
    "y": 300,
    "attack": False
}

other_player = {}

# Receive data from server
def receive():
    global other_player
    while True:
        try:
            data = client.recv(4096)
            if not data:
                break
            other_player = pickle.loads(data)
        except:
            print("Disconnected.")
            break

# Send data to server
def send():
    while True:
        try:
            data = pickle.dumps(player_data)
            client.sendall(data)
        except:
            break

# Start threads
threading.Thread(target=receive, daemon=True).start()
threading.Thread(target=send, daemon=True).start()
