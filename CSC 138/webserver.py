#import socket module
from socket import * 
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
#Fill in start

serverPort = 80 #Assign a port number.
serverSocket.bind(('', serverPort)) #Bind the socket to server address and server port.
serverSocket.listen(1) #Listen to 1 connection at a time.
#^Server begins listening for incoming TCP requests.

#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Server waits on accept() for incoming requests.
    #^New socket created on return!
    try:
        message = connectionSocket.recv(1024) #Read bytes from socket (but not address as in UDP).
        filename = message.split()[1]
        f = open(filename[1:]) 
        outputdata = f.read()#Returns the specified number of bytes from the file. 
        #Send one HTTP header line into socket
        #Fill in start

        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())#HTTP response header line.

        #Fill in end 
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        #Fill in start

        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
        
        #Fill in end
        #Close client socket
        #Fill in start
        
        connectionSocket.close()
        
        #Fill in end 
serverSocket.close()