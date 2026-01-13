import socket
import os

HOST = "127.0.0.1"
PORT = 8200

def main():
    while True:
        file_path = input("Enter file name: ")

        if not os.path.isfile(file_path):
            print("Error: File not found!")
            continue

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((HOST, PORT))
                
                client.sendall(os.path.basename(file_path).encode())

                response = client.recv(1024).decode()

                if response == "EXISTS":
                    print("Error: File already exists on server!")
                elif response == "READY":
                    with open(file_path, "rb") as f:
                        print("Sending...")
                        while True:
                            chunk = f.read(4096)
                            if not chunk:
                                break
                            client.sendall(chunk)
                    print("File sent successfully.")
                
        except ConnectionRefusedError:
            print("Error: Could not connect to server")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
