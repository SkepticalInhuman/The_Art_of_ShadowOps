import socket 

def send_image(image_path, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:       #creating a socket object that will use IPv4 address and TCP protocol and using 'with' so that we don't need to manually close the socket
        s.connect((host, port))                                        #connecting to the server
        with open(image_path, 'rb') as f:                              #opening the image file in the read(binary) mode and 'with' ensures it closes after the code execution
            while (chunk := f.read(1024)):                             #reading the image file in sizes of 1024 bytes till the end of file is reached.':=' operator assigns the 'f.read(1024)' to chunk and passes chunk as an argument to 'while' at the same time.
                s.sendall(chunk)                                       #sending the image chunks
    print("Image sent")
    
if __name__ == "__main__":
    send_image('test.jpg', 'localhost', 65432)                         #calling the fuction with 'localhost' as the host name of the server and port number 65432 on which the server is listening

