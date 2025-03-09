class FileTransfer:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port

    def send_file(self, file_path):
        import socket
        import os

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            file_size = os.path.getsize(file_path)
            s.sendall(f"{os.path.basename(file_path)}:{file_size}".encode())
            with open(file_path, 'rb') as f:
                while (data := f.read(1024)):
                    s.sendall(data)

    def receive_file(self):
        import socket

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                file_info = conn.recv(1024).decode()
                file_name, file_size = file_info.split(':')
                file_size = int(file_size)

                with open(file_name, 'wb') as f:
                    bytes_received = 0
                    while bytes_received < file_size:
                        data = conn.recv(1024)
                        f.write(data)
                        bytes_received += len(data)