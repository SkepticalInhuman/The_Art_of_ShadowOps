import socket
import ssl

def send_image(image_path , host , port):
    context = ssl.create_default_context ()
    with socket.create_connection ((host , port)) as sock:
        with context.wrap_socket(sock , server_hostname=host) as ssock:
            with open(image_path , 'rb') as f:
                while chunk := f.read (4096):
                    ssock.sendall(chunk)
            print("Image sent successfully.")

send_image('path/to/image.jpg', 'receiver_host', 12345)