import socket
import os

HOST = "127.0.0.1"
PORT = 8200

def main():

    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Server is up on {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            with conn:
                print(f"File sent by: {addr}")
                
                filename= conn.recv(1024).decode()
                if not filename:
                    continue
                
                filepath = os.path.join("uploads", filename)

                if os.path.exists(filepath):
                    conn.sendall(b"EXISTS")
                    print(f"Rejected: {filename} (Already exists)")
                else:
                    conn.sendall(b"READY")
                    
                    with open(filepath, "wb") as f:
                        while True:
                            data = conn.recv(4096)
                            if not data: 
                                break
                            f.write(data)
                    print(f"Saved: {filename}")

if __name__ == "__main__":
    main()
