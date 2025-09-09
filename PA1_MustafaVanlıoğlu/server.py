import socket
import pandas as pd
import time

# Read the Excel file (must be in the same directory)
df = pd.read_excel("weathers.xlsx")

HOST = '127.0.0.1' # localhost
PORT = 8888 # Server's port
end_value = 1  # Will be set to 0 if "END" command is received

def handle_request(client_connection, city, actual_temp):
    global end_value
    guess_count = 0
    tolerance = 0.10  # 10% tolerance

    while True:
        data = client_connection.recv(1024).decode().strip()
        if not data:
            break

        if data.upper() == "END":
            print("[SERVER] Client ended the connection.")
            client_connection.sendall("Connection closed.".encode())
            end_value = 0  # Stop the server
            return

        try:
            guess = float(data)
            guess_count += 1
            tolerance_value = actual_temp * tolerance

            # Accept as correct if within tolerance range
            if (actual_temp - tolerance_value) <= guess <= (actual_temp + tolerance_value):
                client_connection.sendall(f"Correct! The temperature in {city} is {actual_temp}°C".encode())
                return

            # End the game if 3 attempts are used
            if guess_count >= 3:
                client_connection.sendall(f"Incorrect 3 times! The correct temperature was {actual_temp}°C".encode())
                time.sleep(0.5)
                return

            # Give feedback to user
            if guess > actual_temp:
                client_connection.sendall("Lower".encode())
            else:
                client_connection.sendall("Higher".encode())

        except ValueError:
            client_connection.sendall("Please enter a valid number or 'END' to exit.".encode())

def serve_forever():
    global end_value

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[SERVER] Listening on {HOST}:{PORT}...")

    while end_value == 1:
        conn, addr = server_socket.accept()
        print(f"[SERVER] Connected by {addr}")

        # Select a random city
        selected = df.sample().iloc[0]
        city = selected['City']
        actual_temp = selected['Temp']

        # Send the city to the client
        conn.sendall(f"Predict the temperature for {city}".encode())

        # Handle guesses from the client
        handle_request(conn, city, actual_temp)

        # Close the connection
        conn.close()

        # Don't show this message if "END" was entered
        if end_value == 1:
            print("[SERVER] Waiting for a new client...")

    server_socket.close()
    print("[SERVER] Shutdown. Bye!")

if __name__ == "__main__":
    serve_forever()
