import socket

HOST = '127.0.0.1'  # localhost
PORT = 8888         # Server's port

def main():   
    try:
        # Create socket and connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        # Receive city information from the server
        data = client_socket.recv(1024).decode()
        if not data:
            print("[CLIENT] Server closed the connection.")
            client_socket.close()
            return

        print(f"[SERVER]: {data}")

        while True:
            guess = input("Your guess (or type END to quit): ").strip()

            # Send the guess to the server
            client_socket.sendall(guess.encode())

            # Receive the response from the server
            response = client_socket.recv(1024).decode()
            if not response:
                print("[CLIENT] Server closed the connection.")
                break

            print(f"[SERVER]: {response}")

            if ("Correct!" in response or 
                "Incorrect 3 times!" in response or 
                "Connection closed." in response):
                break

    except Exception as e:
        print(f"[CLIENT] Error: {e}")

    client_socket.close()
    print("[CLIENT] Disconnected.")

if __name__ == "__main__":
    main()
