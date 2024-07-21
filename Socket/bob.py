import socket 

def recv_image(save_path, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:             #creating a socket object that will use IPv4 address and TCP protocol and using 'with' so that we don't need to manually close the socket
        s.bind((host, port))                                                 #binding the socket so that it will listen on this host and port
        s.listen()                                                           #listening for  connection requests
        conn, addr = s.accept()                                              #accepting a connection request and returns a new socket object conn and address of the client
        with conn:                                                           
            print(f"Connected by {addr}")                                    
            with open(save_path, 'wb') as f:                                 #opening the file specified by the save path(or creating it if it doesn't exist) in the write(binary) mode and 'with' ensures it closes after the code execution
                while (chunk := conn.recv(1024)):                            #receiving the data from conn in sizes of 1024 bytes till no more data is received.':=' operator assigns the 'conn.recv(1024)' to chunk and passes chunk as an argument to 'while' at the same time.
                    f.write(chunk)                                           #writing the received chunk of data to the specified file.
    print("Image received and saved")

if __name__ == "__main__":
    recv_image("C:/Users/USER/OneDrive/Desktop/soc/Socket/received_test.jpg", "localhost", 65432)     #calling the fuction with 'localhost' as the host name of the server and port number 65432 on which the server is listening
