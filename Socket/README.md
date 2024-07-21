# Socket
An image file is sent by the client(Alice) to the server(Bob) using socket programming

## Alice
This is the client side python file. It contains a function send_image with arguments - image path, hostname and port. Initially a socket object that will use Ipv4 address and TCP protocol is created. TCP protocol is used since it ensures all the data sent by the sender is received by the receiver and in order.
'with' statement is used for the socket so that it we don't have to manually close the socket. Aconnection is then established between the socket and the server with the specified host and port. Lower port numbers are reserved which is why a high port number is used.
The image file is then opened in binary read mode and data is read and sent to the server in chunks of 1024 bytes. When all data is read the while loop breaks and an "Image sent" message is printed. The while loop uses a ":=" operator which allows for assignment and to be passed as argument to the while loop. The file and the socket closes on its own since they were used with a 'with' statement.

## Bob
This is the server side python file. It contains a function with rev_image with arguments - image path, hostname and port. Initially a socket object is created that uses IPv4 address and TCP protocol. The socket objest is then binded to the specified hostname and port.
It then listens for connection requests. Connection request is accepted and a new socket object and the address of the client is returened. Then new socket object is used to receive data from the client. Address of the client is printed which is a tuple that contains the IP address and the port number of the client. Data is received in chunks of size 1024 bytes which is then written to the specified file which is opened in binary write mode.
When all data is received, the wbile loop breaks and a message - "Image received and saved" is printed. The while loop uses a ":=" operator which allows for assignment and to be passed as argument to the while loop. When all data is received, both sockets and file closes.

Bob.py is first run to set up the server and then Alice is run to set up the client, connect to the server and send the image. 'test.jpg' is the image file to be sent.
![image](https://github.com/user-attachments/assets/857594db-8764-406f-9557-3bad4d05df5b)

