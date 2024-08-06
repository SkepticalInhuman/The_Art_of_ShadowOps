import socket
import ssl
import sys

def receive_image(save_path , host , port):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="path/to/cert.pem", keyfile="path/to/key.pem")

    with socket.create_server ((host , port)) as server:
        with context.wrap_socket(server , server_side=True) as ssock:
            conn , addr = ssock.accept ()
            with conn:
                with open(save_path , 'wb') as f:
                    while chunk := conn.recv (4096):
                        f.write(chunk)
            print("Image received successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python receiver.py <save_path > <host > <port >")
        sys.exit (1)

    save_path = sys.argv [1]
    host = sys.argv [2]
    port = int(sys.argv [3])

    receive_image(save_path , host , port)